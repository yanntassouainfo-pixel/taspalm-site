
/* Taspalm · L'Exploitation · mouvement, menu, index produits · Yann Tassoua 2026-09 */
(function(){
  var reduit=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var capture=innerHeight>1800;
  var els=[].slice.call(document.querySelectorAll('[data-px],[data-pxx]'));
  var rev=[].slice.call(document.querySelectorAll('[data-reveal]'));
  function tout(){rev.forEach(function(e){e.classList.add('vu')})}
  if(reduit||capture){tout();}
  else{
    function cadre(){
      if(innerWidth<900){els.forEach(function(e){e.style.transform=''});return;}
      var vh=innerHeight;
      els.forEach(function(e){
        var r=e.getBoundingClientRect(); if(r.bottom<-200||r.top>vh+200)return;
        var c=r.top+r.height/2-vh/2;
        var y=e.dataset.px?-c*parseFloat(e.dataset.px):0, x=e.dataset.pxx?-c*parseFloat(e.dataset.pxx):0;
        e.style.transform='translate3d('+x.toFixed(1)+'px,'+y.toFixed(1)+'px,0) '+(e.dataset.rot||'');
      });
    }
    var att=false;
    addEventListener('scroll',function(){if(!att){requestAnimationFrame(function(){cadre();att=false});att=true}},{passive:true});
    addEventListener('resize',cadre);
    var io=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){x.target.classList.add('vu');io.unobserve(x.target)}})},{threshold:.15});
    rev.forEach(function(e){io.observe(e)});
    cadre();
  }
  /* menu mobile */
  var nav=document.querySelector('nav'),b=document.querySelector('.burger');
  if(b){b.addEventListener('click',function(){nav.classList.toggle('ouvert');b.textContent=nav.classList.contains('ouvert')?(b.dataset.fermer||'Fermer'):(b.dataset.menu||'Menu');});}
  /* nav collante : visible en remontant, masquée en descendant, jamais sur le héros */
  (function(){
    var seuil=nav.offsetHeight+40, prec=scrollY, tick=false;
    function maj(){
      var y=scrollY;
      if(y<=seuil){nav.classList.remove('colle','cachee');}
      else{
        nav.classList.add('colle');
        if(y>prec+4 && !nav.classList.contains('ouvert')) nav.classList.add('cachee');
        else if(y<prec-4) nav.classList.remove('cachee');
      }
      prec=y; tick=false;
    }
    addEventListener('scroll',function(){if(!tick){requestAnimationFrame(maj);tick=true;}},{passive:true});
    maj();
  })();
  /* index produits : entrée active */
  var idx=document.querySelectorAll('.index a');
  if(idx.length){
    var cibles=[].slice.call(idx).map(function(a){return document.querySelector(a.getAttribute('href'))}).filter(Boolean);
    var io2=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){idx.forEach(function(a){a.classList.toggle('actif',a.getAttribute('href')==='#'+x.target.id)})}})},{rootMargin:'-40% 0px -50% 0px'});
    cibles.forEach(function(c){io2.observe(c)});
  }
})();
