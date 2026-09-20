
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
  if(b){b.dataset.menu=b.dataset.menu||b.textContent;b.addEventListener('click',function(){var o=nav.classList.toggle('ouvert');document.documentElement.classList.toggle('menu-ouvert',o);b.setAttribute('aria-expanded',o?'true':'false');b.textContent=o?(b.dataset.fermer||'Fermer'):b.dataset.menu;});
    [].slice.call(nav.querySelectorAll('ul a')).forEach(function(a){a.addEventListener('click',function(){if(nav.classList.contains('ouvert')){nav.classList.remove('ouvert');document.documentElement.classList.remove('menu-ouvert');b.setAttribute('aria-expanded','false');b.textContent=b.dataset.menu;}});});}
  /* carrousels mobiles : un point par carte, le point actif suit le défilement */
  [].slice.call(document.querySelectorAll('.etapes,.publics,.chrono ol,.grille3,.produits .defile')).forEach(function(c){
    var n=c.children.length; if(n<2)return;
    var p=document.createElement('div'); p.className='points'; p.setAttribute('aria-hidden','true');
    c.classList.add('carrousel');
    for(var k=0;k<n;k++){p.appendChild(document.createElement('i'));}
    (c.parentNode.classList.contains('chrono')?c.parentNode:c).insertAdjacentElement('afterend',p);
    function maj(){var w=c.children[0].getBoundingClientRect().width+14,k=Math.round(c.scrollLeft/w);k=Math.min(k,n-1);[].forEach.call(p.children,function(i,x){i.classList.toggle('on',x===k);});[].forEach.call(c.children,function(e,x){e.classList.toggle('actif',x===k);});}
    c.addEventListener('scroll',function(){requestAnimationFrame(maj);},{passive:true}); maj();
  });
  /* flèche de retour en haut : elle ne se montre que lorsque le pied de page entre à l'écran */
  (function(){
    var b=document.querySelector('.haut'), pied=document.querySelector('footer');
    if(!b||!pied||!('IntersectionObserver' in window)) return;
    new IntersectionObserver(function(e){ b.classList.toggle('vue', e[0].isIntersecting); }, {threshold:0}).observe(pied);
    b.addEventListener('click', function(){
      var doux = !window.matchMedia('(prefers-reduced-motion: reduce)').matches;
      window.scrollTo({top:0, behavior: doux ? 'smooth' : 'auto'});
    });
  })();
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
  /* formulaires : horodatage anti-robot et page d'origine */
  [].slice.call(document.querySelectorAll('form.form')).forEach(function(f){var t=f.querySelector('[name=t]'),p=f.querySelector('[name=page]');if(t)t.value=Date.now();if(p)p.value=location.pathname;});
  if(/[?&]envoi=erreur/.test(location.search)){var al=document.getElementById('alerte-envoi');if(al){al.hidden=false;al.scrollIntoView({block:'center'});}}
  /* index produits : entrée active */
  var idx=document.querySelectorAll('.index a');
  if(idx.length){
    var cibles=[].slice.call(idx).map(function(a){return document.querySelector(a.getAttribute('href'))}).filter(Boolean);
    var io2=new IntersectionObserver(function(en){en.forEach(function(x){if(x.isIntersecting){idx.forEach(function(a){a.classList.toggle('actif',a.getAttribute('href')==='#'+x.target.id)})}})},{rootMargin:'-40% 0px -50% 0px'});
    cibles.forEach(function(c){io2.observe(c)});
  }
})();
