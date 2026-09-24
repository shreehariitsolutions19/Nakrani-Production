document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('site-nav');
  const toggle = document.querySelector('.mobile-toggle');
  const panel = document.getElementById('mobile-panel');
  const icon = toggle ? toggle.querySelector('i') : null;
  const onScroll = () => nav && nav.classList.toggle('scrolled', window.scrollY > 20);
  onScroll();
  window.addEventListener('scroll', onScroll, { passive: true });

  if (toggle && panel) {
    toggle.addEventListener('click', () => {
      const open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      if (icon) icon.className = open ? 'ri-close-line' : 'ri-menu-3-line';
    });
    panel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => panel.classList.remove('open')));
  }

  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) entry.target.classList.add('in-view');
    });
  }, { threshold: 0.12 });

  document.querySelectorAll('.reveal, .animate-element').forEach(el => observer.observe(el));

  const faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(item => {
    const button = item.querySelector('.faq-question');
    if (!button) return;
    button.addEventListener('click', () => {
      const isOpen = item.classList.contains('is-open');
      faqItems.forEach(entry => {
        const q = entry.querySelector('.faq-question');
        const openState = entry === item ? !isOpen : false;
        entry.classList.toggle('is-open', openState);
        if (q) q.setAttribute('aria-expanded', String(openState));
      });
    });
  });

  const finePointer = window.matchMedia('(pointer:fine)').matches;
  if (finePointer) {
    const motionState = {
      currentX: 0,
      currentY: 0,
      targetX: 0,
      targetY: 0,
      rafId: null,
    };

    const parallaxEls = document.querySelectorAll('[data-parallax]');

    const updateMotion = () => {
      motionState.currentX += (motionState.targetX - motionState.currentX) * 0.08;
      motionState.currentY += (motionState.targetY - motionState.currentY) * 0.08;

      parallaxEls.forEach(el => {
        const strength = Number(el.dataset.parallax || 0);
        const tx = motionState.currentX * strength;
        const ty = motionState.currentY * strength;
        // Write to CSS variables instead of overwriting `transform` directly,
        // so each element's own rotation / hover transforms keep working.
        // Elements should use e.g. transform: translate3d(var(--px,0px), var(--py,0px), 0) rotate(...)
        el.style.setProperty('--px', `${tx}px`);
        el.style.setProperty('--py', `${ty}px`);
      });

      motionState.rafId = requestAnimationFrame(updateMotion);
    };

    window.addEventListener('pointermove', event => {
      const x = (event.clientX / window.innerWidth) - 0.5;
      const y = (event.clientY / window.innerHeight) - 0.5;
      motionState.targetX = x;
      motionState.targetY = y;
      if (!motionState.rafId) {
        motionState.rafId = requestAnimationFrame(updateMotion);
      }
    });

    window.addEventListener('pointerleave', () => {
      motionState.targetX = 0;
      motionState.targetY = 0;
    });
  }
});