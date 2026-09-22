document.addEventListener('DOMContentLoaded', () => {
  const nav = document.getElementById('site-nav');
  const toggle = document.querySelector('.mobile-toggle');
  const panel = document.getElementById('mobile-panel');
  const icon = toggle ? toggle.querySelector('i') : null;
  const onScroll = () => nav && nav.classList.toggle('scrolled', window.scrollY > 20);
  onScroll(); window.addEventListener('scroll', onScroll, {passive:true});
  if (toggle && panel) {
    toggle.addEventListener('click', () => {
      const open = panel.classList.toggle('open');
      toggle.setAttribute('aria-expanded', String(open));
      if (icon) icon.className = open ? 'ri-close-line' : 'ri-menu-3-line';
    });
    panel.querySelectorAll('a').forEach(a => a.addEventListener('click', () => panel.classList.remove('open')));
  }
  const observer = new IntersectionObserver(entries => entries.forEach(entry => { if (entry.isIntersecting) entry.target.classList.add('in-view'); }), {threshold:.12});
  document.querySelectorAll('.reveal, .animate-element').forEach(el => observer.observe(el));
  const finePointer = window.matchMedia('(pointer:fine)').matches;
  if (finePointer) {
    document.querySelectorAll('[data-parallax]').forEach(card => {
      const strength = Number(card.dataset.parallax || 12);
      card.addEventListener('mousemove', e => {
        const r = card.getBoundingClientRect();
        const x = (e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
        card.style.transform = `translate3d(${x*strength}px,${y*strength}px,0)`;
      });
      card.addEventListener('mouseleave', () => card.style.transform = 'translate3d(0,0,0)');
    });
    const hero = document.querySelector('.hero-floating-zone');
    if (hero) {
      const cards = [...hero.querySelectorAll('.floating-card')];
      const base = cards.map(card => card.style.transform || '');
      hero.addEventListener('mousemove', e => {
        const r = hero.getBoundingClientRect();
        const x = (e.clientX-r.left)/r.width-.5, y=(e.clientY-r.top)/r.height-.5;
        cards.forEach((card,i) => {
          const power = 4 + i * 1.1;
          card.style.transform = `${base[i]} translate3d(${x*power}px,${y*power}px,0)`;
        });
      });
      hero.addEventListener('mouseleave', () => cards.forEach((card,i) => card.style.transform = base[i]));
    }
  }
});
