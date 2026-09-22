document.addEventListener('DOMContentLoaded',()=>{
 const header=document.querySelector('.site-header');
 const menu=document.querySelector('.menu');
 const nav=document.querySelector('.nav-links');
 const onScroll=()=>header?.classList.toggle('scrolled',window.scrollY>30);
 window.addEventListener('scroll',onScroll,{passive:true}); onScroll();
 menu?.addEventListener('click',()=>nav?.classList.toggle('open'));
 document.querySelectorAll('.reveal').forEach(el=>{
   const io=new IntersectionObserver(entries=>entries.forEach(e=>{if(e.isIntersecting){e.target.classList.add('show');io.unobserve(e.target)}}),{threshold:.12}); io.observe(el);
 });
 const art=document.querySelector('.hero-art');
 if(art && matchMedia('(pointer:fine)').matches){
   const cards=[...art.querySelectorAll('.art-card')];
   art.addEventListener('mousemove',e=>{const r=art.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;cards.forEach((c,i)=>c.style.transform=`translate(${x*(i+1)*12}px,${y*(i+1)*9}px) rotate(${i===0?-8:i===1?6:-1}deg)`)});
   art.addEventListener('mouseleave',()=>cards.forEach((c,i)=>c.style.transform=`rotate(${i===0?-8:i===1?6:-1}deg)`));
 }
 document.querySelectorAll('a[href]').forEach(a=>{a.addEventListener('click',()=>nav?.classList.remove('open'))});
});
