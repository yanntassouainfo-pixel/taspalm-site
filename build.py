# -*- coding: utf-8 -*-
"""Taspalm · direction A « L'Exploitation » · générateur du site complet (maquettes HTML).
Sortie : site-A/www/  (pages, styles.css, site.js, images/*.jpg)
Yann Tassoua · 2026-09-17
"""
import os, shutil, re
from PIL import Image

B = os.path.dirname(os.path.abspath(__file__))
SRC_IMG = os.path.join(B, "images-source")
WWW = os.path.join(B, "www")
os.makedirs(os.path.join(WWW, "images"), exist_ok=True)
os.makedirs(os.path.join(WWW, "fonts"), exist_ok=True)
if os.path.isdir(os.path.join(B, "images-reelles")):
    for f in os.listdir(os.path.join(B, "images-reelles")):
        if f.endswith(".jpg"): shutil.copy(os.path.join(B, "images-reelles", f), os.path.join(WWW, "images", f))
if os.path.isdir(os.path.join(B, "images-hero")):
    for f in os.listdir(os.path.join(B, "images-hero")):
        if f.endswith((".jpg",".webp")): shutil.copy(os.path.join(B, "images-hero", f), os.path.join(WWW, "images", f))
for f in os.listdir(os.path.join(B, "fonts")):
    if f.endswith(".woff2"): shutil.copy(os.path.join(B, "fonts", f), os.path.join(WWW, "fonts", f))

# ---------------------------------------------------------------- images (png → jpg)
for f in sorted(os.listdir(SRC_IMG)):
    if f.endswith(".png"):
        dst = os.path.join(WWW, "images", f[:-4] + ".jpg")
        if not os.path.exists(dst):
            Image.open(os.path.join(SRC_IMG, f)).convert("RGB").save(dst, quality=86)

# ---------------------------------------------------------------- CSS
CSS = r"""
@font-face{font-family:"Cormorant Garamond";font-style:normal;font-weight:400 600;font-display:swap;src:url(fonts/cormorant-garamond.woff2) format("woff2")}
@font-face{font-family:"Cormorant Garamond";font-style:italic;font-weight:400;font-display:swap;src:url(fonts/cormorant-garamond-italic.woff2) format("woff2")}
@font-face{font-family:Manrope;font-style:normal;font-weight:400 600;font-display:swap;src:url(fonts/manrope.woff2) format("woff2")}
:root{--vert:#0E2E24;--vert2:#16402F;--creme:#F4EFE4;--creme2:#EAE2D1;--or:#C89A3A;--terre:#7A4A2A;--encre:#1C1A16;--encre2:#5B564C;--trait:#D9D0BC;--voile:rgba(14,46,36,.55)}
*{box-sizing:border-box;margin:0;padding:0}
html{scroll-behavior:smooth}
html,body{overflow-x:clip}
body{background:var(--creme);color:var(--encre);font:400 17px/1.6 Manrope,Helvetica,Arial,sans-serif;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4,.serif{font-family:"Cormorant Garamond",Georgia,serif;font-weight:500;line-height:1.05;text-wrap:balance}
em{font-style:italic}
a{color:inherit;text-decoration:none}
img{display:block;max-width:100%}
.sur{font:600 11px/1 Manrope,sans-serif;letter-spacing:.22em;text-transform:uppercase;color:var(--or)}
.wrap{width:min(1240px,calc(100% - 200px));margin:0 auto}
.btn{display:inline-block;padding:16px 28px;border-radius:2px;font:600 12.5px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;transition:transform .35s,background .35s,color .35s}
.btn:hover{transform:translateY(-2px)}
.btn.or{background:var(--or);color:var(--vert)}
.btn.ghost{border:1px solid rgba(244,239,228,.5);color:var(--creme)}
.btn.vert{background:var(--vert);color:var(--creme)}
.btn.ligne{border:1px solid var(--vert);color:var(--vert)}
.lien{font:600 12px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--terre);border-bottom:1px solid var(--terre);padding-bottom:5px}
.lien.clair{color:var(--or);border-color:var(--or)}
.attente{color:#9A9282;font-family:Manrope,sans-serif;font-weight:500;letter-spacing:.06em;font-size:.72em}
.tag{display:inline-block;font:600 10px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;padding:6px 9px;border-radius:2px;background:var(--creme2);color:var(--encre2);vertical-align:middle;margin-left:8px}
.tag.n{background:#F2DCCB;color:#8A3A18}
/* ---- nav ---- */
nav{position:absolute;top:0;left:0;right:0;z-index:20;display:flex;align-items:center;justify-content:space-between;padding:28px 100px;color:var(--creme)}
nav .logo{display:flex;align-items:center;gap:14px}
nav .logo .mono{width:38px;height:38px;border:1.5px solid var(--or);border-radius:50%;display:grid;place-items:center;font-family:"Cormorant Garamond",serif;font-size:22px;color:var(--or)}
nav .logo b{font-family:"Cormorant Garamond",serif;font-size:26px;letter-spacing:.14em;font-weight:500}
nav ul{display:flex;gap:38px;list-style:none;font:500 14px/1 Manrope,sans-serif;letter-spacing:.06em;white-space:nowrap}
nav .logo,nav .droite{flex-shrink:0}nav .cta,nav .lang{white-space:nowrap}nav{gap:24px}
nav ul a{padding-bottom:6px;border-bottom:1px solid transparent;transition:border-color .3s}
nav ul a:hover,nav ul a.ici{border-bottom-color:var(--or)}
nav .cta{border:1px solid var(--or);color:var(--or);padding:12px 22px;border-radius:2px;font:600 12px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase}
nav .lang{font:600 12px/1 Manrope,sans-serif;letter-spacing:.14em;color:var(--creme);border:1px solid rgba(244,239,228,.45);padding:11px 12px;border-radius:2px;margin-left:-16px}
nav .droite{display:flex;align-items:center;gap:26px}
/* nav collante : apparaît quand on remonte, disparaît quand on descend (site.js pose .colle / .cachee) */
nav.colle{position:fixed;top:0;padding:14px 100px;background:rgba(244,239,228,.94);color:var(--vert);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);border-bottom:1px solid var(--trait);box-shadow:0 2px 14px rgba(28,26,22,.06);transform:translateY(0);transition:transform .32s cubic-bezier(.2,.7,.2,1),background .32s,padding .32s}
nav.colle.cachee{transform:translateY(-105%)}
nav.colle .logo b{font-size:22px}
nav.colle .logo .mono{width:32px;height:32px;font-size:19px;border-color:var(--vert);color:var(--vert)}
nav.colle ul a{color:var(--vert)}nav.colle ul a:hover,nav.colle ul a.ici{border-bottom-color:var(--terre)}
nav.colle .cta{border-color:var(--vert);color:var(--vert);padding:10px 18px}
nav.colle .lang{color:var(--vert);border-color:rgba(14,46,36,.4)}
nav.colle .burger{color:var(--vert);border-color:rgba(14,46,36,.4)}
nav.ouvert{color:var(--creme)}nav.ouvert.colle{background:var(--vert)}nav.ouvert .burger{color:var(--creme);border-color:rgba(244,239,228,.5)}
@media (prefers-reduced-motion:reduce){nav.colle{transition:none}}
.barre-action{display:none}
.indice{display:none}
nav .burger{display:none;width:44px;height:44px;border:1px solid rgba(244,239,228,.5);border-radius:2px;background:none;color:var(--creme);cursor:pointer;font:600 11px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase}
/* ---- hero ---- */
.hero{position:relative;min-height:860px;background:var(--vert);overflow:hidden;color:var(--creme);display:flex;align-items:flex-end}
.hero.court{min-height:640px}
.hero>img,.hero>picture>img{position:absolute;left:0;width:100%;top:-14%;height:128%;object-fit:cover;object-position:center 40%;opacity:.92;z-index:0}
.hero:after{content:"";position:absolute;left:0;right:0;top:0;height:180px;background:linear-gradient(180deg,rgba(14,46,36,.75),rgba(14,46,36,0));z-index:2;pointer-events:none}
.hero .txt,.hero .origine{z-index:3}
.hero .voile{position:absolute;inset:0;z-index:1;background:linear-gradient(90deg,rgba(9,30,23,.95) 0%,rgba(9,30,23,.84) 34%,rgba(9,30,23,.5) 62%,rgba(9,30,23,.18) 100%),linear-gradient(180deg,rgba(9,30,23,0) 55%,rgba(9,30,23,.55) 100%)}
.hero .voile.bas{background:linear-gradient(90deg,rgba(9,30,23,.9) 0%,rgba(9,30,23,.72) 40%,rgba(9,30,23,.3) 100%),linear-gradient(180deg,rgba(9,30,23,.2) 0%,rgba(9,30,23,.5) 50%,rgba(9,30,23,.9) 100%)}
.hero .txt{position:relative;padding:0 100px 110px;width:min(760px,100%)}
.hero .fil{font:500 12px/1 Manrope,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:rgba(244,239,228,.6);margin-bottom:20px}
.hero .fil a{color:var(--or)}
.hero h1{font-size:78px;letter-spacing:-.01em;margin:18px 0 22px;text-shadow:0 2px 24px rgba(0,0,0,.45)}
.hero h1 em{color:#E2B559}
.hero.court h1{font-size:68px}
.hero h1 em{color:var(--or);font-weight:400}
.hero p{font-size:19px;line-height:1.55;color:rgba(250,246,238,.96);max-width:540px;text-shadow:0 1px 14px rgba(0,0,0,.5)}
.hero .actions{display:flex;gap:16px;margin-top:34px;flex-wrap:wrap}
.hero .origine{position:absolute;right:100px;bottom:110px;text-align:right;font:500 12px/1.7 Manrope,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:rgba(244,239,228,.7)}
.hero .origine b{display:block;font-family:"Cormorant Garamond",serif;font-size:30px;letter-spacing:0;text-transform:none;color:var(--creme);font-weight:400}
.hero .titre-anim>*{opacity:0;transform:translateY(26px);animation:monter 1.1s cubic-bezier(.2,.7,.2,1) forwards}
.hero .titre-anim>*:nth-child(2){animation-delay:.15s}.hero .titre-anim>*:nth-child(3){animation-delay:.3s}.hero .titre-anim>*:nth-child(4){animation-delay:.45s}.hero .titre-anim>*:nth-child(5){animation-delay:.6s}
@keyframes monter{to{opacity:1;transform:none}}
/* ---- bandeau défilant ---- */
.bande{background:var(--or);color:var(--vert);padding:18px 0;font:600 12px/1 Manrope,sans-serif;letter-spacing:.2em;text-transform:uppercase;overflow:hidden;white-space:nowrap}
.bande .piste{display:inline-flex;animation:defiler 38s linear infinite}
.bande span{padding:0 28px}
@keyframes defiler{to{transform:translateX(-50%)}}
/* ---- sections ---- */
section{padding:120px 0}
section.serre{padding:90px 0}
.sombre{background:var(--vert);color:var(--creme)}
.sombre .sur{color:var(--or)}
.sombre p{color:rgba(244,239,228,.82)}
.encre{background:var(--encre);color:var(--creme)}
.tete{display:flex;justify-content:space-between;align-items:flex-end;gap:60px;margin-bottom:56px}
.tete h2{font-size:62px;max-width:700px}
.tete p{max-width:400px;color:var(--encre2);font-size:16px}
.sombre .tete p,.encre .tete p{color:rgba(244,239,228,.7)}
h2 em{font-weight:400;color:var(--terre)}
.sombre h2 em{color:var(--or)}
.deux{display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:center}
.deux h2{font-size:58px;margin:16px 0 26px}
.deux p{margin-bottom:16px}
.photo{position:relative;border-radius:3px;overflow:hidden;height:620px;background:var(--creme2)}
.photo>img{position:absolute;left:0;width:100%;top:-14%;height:128%;object-fit:cover}
.photo .leg{position:absolute;left:0;right:0;bottom:0;padding:16px 20px;font:500 11px/1.5 Manrope,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:#FAF6EE;background:linear-gradient(180deg,rgba(20,18,14,0),rgba(20,18,14,.55) 45%,rgba(20,18,14,.88));padding-top:44px;font-size:11.5px;font-weight:600;text-shadow:0 1px 6px rgba(0,0,0,.6)}
/* collection */
.grille3{display:grid;grid-template-columns:1.35fr 1fr 1fr;gap:26px}
.card{position:relative;background:var(--creme2);border-radius:3px;overflow:hidden;min-height:520px;display:flex;flex-direction:column;justify-content:flex-end}
.card img{position:absolute;left:0;width:100%;top:-8%;height:116%;object-fit:cover;transition:transform 1.2s cubic-bezier(.2,.7,.2,1)}
.card:hover img{transform:scale(1.04)}
.card .cap{position:relative;padding:70px 28px 26px;background:linear-gradient(180deg,rgba(20,18,14,0) 0%,rgba(20,18,14,.7) 38%,rgba(20,18,14,.92) 100%);color:#FAF6EE;text-shadow:0 1px 8px rgba(0,0,0,.55)}
.card .cap .sur{color:var(--or)}
.card .cap h3{font-size:34px;margin:8px 0 6px}
.card .cap p{font-size:14.5px;color:rgba(250,246,238,.94)}
.autres{display:flex;margin-top:26px;border-top:1px solid var(--trait);border-bottom:1px solid var(--trait)}
.autres a{flex:1;padding:22px 0;text-align:center;border-right:1px solid var(--trait);transition:background .3s}
.autres a:hover{background:var(--creme2)}
.autres a:last-child{border-right:0}
.autres b{display:block;font-family:"Cormorant Garamond",serif;font-size:26px;font-weight:500}
.autres span{font:500 11px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--encre2)}
/* faits */
.faits{display:grid;grid-template-columns:1fr 1fr;gap:22px 30px;margin-top:38px;border-top:1px solid rgba(244,239,228,.18);padding-top:30px}
.faits b{display:block;font-family:"Cormorant Garamond",serif;font-size:40px;font-weight:500;color:var(--or);line-height:1}
.faits span{font:500 12px/1.5 Manrope,sans-serif;letter-spacing:.1em;text-transform:uppercase;color:rgba(244,239,228,.65)}
.faits .attente b{color:rgba(244,239,228,.35);font-size:26px;font-family:Manrope,sans-serif;font-weight:500;letter-spacing:.06em}
.clair .faits{border-color:var(--trait)}.clair .faits b{color:var(--terre)}.clair .faits span{color:var(--encre2)}.clair .faits .attente b{color:#9A9282}
/* manifeste */
.manifeste{max-width:980px;margin:0 auto;text-align:center}
.manifeste p{font-family:"Cormorant Garamond",serif;font-size:44px;line-height:1.25;color:var(--encre);margin-bottom:26px}
.manifeste p em{color:var(--terre)}
.sombre .manifeste p{color:var(--creme)}.sombre .manifeste p em{color:var(--or)}
/* étapes horizontales */
.etapes{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.etape .photo{height:420px}
.etape .n{font-family:"Cormorant Garamond",serif;font-size:22px;color:var(--terre);margin:22px 0 8px}
.etape h3{font-size:32px;margin-bottom:10px}
.etape p{color:var(--encre2);font-size:15.5px}
.sombre .etape .n{color:var(--or)}.sombre .etape p{color:rgba(244,239,228,.75)}
/* liste */
.liste{list-style:none;margin-top:30px}
.liste li{padding:22px 0;border-top:1px solid var(--trait);display:flex;justify-content:space-between;align-items:center;gap:30px}
.liste li:last-child{border-bottom:1px solid var(--trait)}
.liste li b{font-family:"Cormorant Garamond",serif;font-size:28px;font-weight:500}
.liste li span{font:600 11px/1.6 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--terre);text-align:right;max-width:46%}
.sombre .liste li{border-color:rgba(244,239,228,.18)}.sombre .liste li span{color:var(--or)}
/* formulaire */
.form{background:var(--creme2);padding:44px;border-radius:3px;color:var(--encre)}
.sombre .form p,.encre .form p{color:var(--encre2)}
.form h3{font-size:30px;margin-bottom:8px}
.form p{font-size:15px;color:var(--encre2)}
.form label{display:block;margin-top:18px;font:600 10.5px/1 Manrope,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--encre2)}
.form input,.form select,.form textarea{width:100%;border:0;border-bottom:1px solid #B9AE95;background:none;padding:12px 0;font:400 15px/1.4 Manrope,sans-serif;color:var(--encre);outline:none}
.form input:focus,.form textarea:focus,.form select:focus{border-bottom-color:var(--vert)}
.form .btn{margin-top:30px;border:0;cursor:pointer;font-family:Manrope,sans-serif}
.form .note a{text-decoration:underline}
.pot{position:absolute;left:-9999px;width:1px;height:1px;overflow:hidden}
.alerte{grid-column:1/-1;background:#F6E0D6;border-left:4px solid #A2452A;color:#5A2412;padding:16px 20px;border-radius:3px;font-size:15px}
.form .note{font-size:12.5px;color:#8D8574;margin-top:16px}
/* fiche produit */
.fiche{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--trait)}
.fiche div{padding:18px 0;border-bottom:1px solid var(--trait);display:grid;grid-template-columns:170px 1fr;gap:20px;align-items:baseline}
.fiche div:nth-child(odd){padding-right:40px}
.fiche div:nth-child(even){padding-left:40px;border-left:1px solid var(--trait)}
.fiche span{font:600 10.5px/1.6 Manrope,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:var(--encre2)}
.fiche b{font-family:"Cormorant Garamond",serif;font-size:24px;font-weight:500}
.fiche b.attente{font-family:Manrope,sans-serif;font-size:14px;font-weight:500}
/* produits : index collant + rangées */
.produits{display:grid;grid-template-columns:260px 1fr;gap:80px;align-items:start}
.index{position:sticky;top:40px}
.index a{display:flex;justify-content:space-between;padding:14px 0;border-top:1px solid var(--trait);font-family:"Cormorant Garamond",serif;font-size:24px;transition:padding-left .3s,color .3s}
.index a:last-child{border-bottom:1px solid var(--trait)}
.index a span{font:500 10.5px/2.4 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--encre2)}
.index a:hover,.index a.actif{padding-left:10px;color:var(--terre)}
.rangee{display:grid;grid-template-columns:1fr 1fr;gap:50px;align-items:center;padding:60px 0;border-top:1px solid var(--trait)}
.rangee:first-child{border-top:0;padding-top:0}
.rangee:nth-child(even) .photo{order:2}
.rangee .photo{height:520px}
.rangee h2{font-size:52px;margin:14px 0 16px}
.rangee p{color:var(--encre2);margin-bottom:14px}
.rangee .mini{display:grid;grid-template-columns:1fr 1fr 1fr;gap:16px;margin:22px 0 26px;border-top:1px solid var(--trait);padding-top:18px}
.rangee .mini span{display:block;font:600 10px/1.6 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--encre2)}
.rangee .mini b{font-family:"Cormorant Garamond",serif;font-size:21px;font-weight:500}
.rangee .mini b.attente{font-family:Manrope,sans-serif;font-size:13px}
/* chronologie */
.chrono{position:relative;margin-top:50px}
.chrono:before{content:"";position:absolute;left:0;right:0;top:34px;height:1px;background:var(--trait)}
.chrono ol{list-style:none;display:grid;grid-template-columns:repeat(5,1fr);gap:24px}
.chrono li{position:relative;padding-top:56px}
.chrono li:before{content:"";position:absolute;left:0;top:28px;width:13px;height:13px;border-radius:50%;background:var(--terre);border:3px solid var(--creme)}
.chrono li.attente:before{background:var(--creme);border:1.5px solid #9A9282}
.chrono b{display:block;font-family:"Cormorant Garamond",serif;font-size:36px;font-weight:500;line-height:1;margin-bottom:10px}
.chrono li.attente b{font-family:Manrope,sans-serif;font-size:16px;color:#9A9282;letter-spacing:.06em;font-weight:500;padding-top:12px}
.chrono p{font-size:14.5px;color:var(--encre2)}
/* portraits à fournir */
.gens{display:grid;grid-template-columns:repeat(3,1fr);gap:26px}
.gens div{background:var(--creme2);border-radius:3px;padding:22px}
.gens .ph{height:300px;border:1px dashed #B9AE95;border-radius:2px;display:grid;place-items:center;font:500 11px/1.6 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#8D8574;text-align:center;padding:20px}
.gens b{display:block;font-family:"Cormorant Garamond",serif;font-size:28px;font-weight:500;margin-top:18px}
.gens span{font:500 11px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--encre2)}
/* carte schématique */
.carte-svg{background:var(--vert2);border-radius:3px;padding:30px;position:relative}
.carte-svg svg{width:100%;height:auto;display:block}
.carte-svg .leg{position:absolute;left:30px;bottom:24px;font:500 11px/1.6 Manrope,sans-serif;letter-spacing:.12em;text-transform:uppercase;color:rgba(244,239,228,.6)}
/* accordéon */
.faq{border-top:1px solid var(--trait)}
.faq details{border-bottom:1px solid var(--trait)}
.faq summary{cursor:pointer;list-style:none;padding:24px 0;font-family:"Cormorant Garamond",serif;font-size:28px;display:flex;justify-content:space-between;align-items:center}
.faq summary::-webkit-details-marker{display:none}
.faq summary:after{content:"+";font-family:Manrope,sans-serif;font-size:22px;color:var(--terre);transition:transform .3s}
.faq details[open] summary:after{transform:rotate(45deg)}
.faq .r{padding:0 0 26px;color:var(--encre2);max-width:760px}
/* publics */
.publics{display:grid;grid-template-columns:repeat(4,1fr);gap:22px}
.public{border:1px solid rgba(244,239,228,.2);border-radius:3px;padding:30px 26px;min-height:320px;display:flex;flex-direction:column}
.public h3{font-size:32px;margin:12px 0 10px}
.public p{font-size:15px;flex:1}
.public .lien{align-self:flex-start;margin-top:22px}
/* pied ---- */
footer{background:var(--encre);color:rgba(244,239,228,.75);padding:70px 0 40px;font-size:14px}
footer .wrap{display:grid;grid-template-columns:1.4fr 1fr 1fr 1fr;gap:40px}
footer b{display:block;color:var(--creme);font-family:"Cormorant Garamond",serif;font-size:26px;font-weight:500;margin-bottom:10px}
footer .sur{color:var(--or);margin-bottom:12px;display:block}
footer p{line-height:1.7}
footer ul{list-style:none;line-height:2}
footer .bas{margin-top:50px;padding-top:20px;border-top:1px solid rgba(244,239,228,.14);display:flex;justify-content:space-between;font-size:12px;color:rgba(244,239,228,.45);flex-wrap:wrap;gap:10px}
.mention{position:fixed;left:0;right:0;bottom:0;z-index:30;background:#B03A2E;color:#fff;font:600 11px/1 Manrope,sans-serif;letter-spacing:.12em;text-transform:uppercase;text-align:center;padding:9px}
/* ---- mouvement ---- */
[data-px],[data-pxx]{will-change:transform}
[data-reveal]{opacity:0;transform:translateY(34px);transition:opacity .9s cubic-bezier(.2,.7,.2,1),transform .9s cubic-bezier(.2,.7,.2,1)}
[data-reveal].vu{opacity:1;transform:none}
.d2{transition-delay:.12s}.d3{transition-delay:.24s}.d4{transition-delay:.36s}.d5{transition-delay:.48s}
.manifeste p[data-reveal]{transform:translateY(18px)}
@media (prefers-reduced-motion:reduce){[data-reveal]{opacity:1;transform:none;transition:none}[data-px],[data-pxx]{transform:none!important}.hero .titre-anim>*{animation:none;opacity:1;transform:none}.bande .piste{animation:none}}
/* ---- composants ajoutés le 19/09 ---- */
nav .logo b{font-size:25px;letter-spacing:.2em}
.menu-plus{display:none}
.une-ligne{white-space:nowrap}
.hero.court .txt{width:min(980px,100%)}
.ico-wa{width:20px;height:20px;flex-shrink:0}
.btn.wa{display:inline-flex;align-items:center;justify-content:center;gap:10px;background:#1F7A4A;color:#fff}
.btn.wa:hover{background:#18623B}
.wa-flottant{position:fixed;right:28px;bottom:28px;z-index:24;display:flex;align-items:center;gap:10px;background:#1F7A4A;color:#fff;border-radius:999px;padding:14px 20px 14px 16px;box-shadow:0 10px 30px rgba(14,46,36,.28);font:600 13px/1 Manrope,sans-serif;letter-spacing:.04em;transition:transform .3s,box-shadow .3s}
.wa-flottant .ico-wa{width:24px;height:24px}
.wa-flottant:hover{transform:translateY(-2px);box-shadow:0 14px 34px rgba(14,46,36,.34)}
footer .tels span{display:block;color:var(--or);font:600 11px/1 Manrope,sans-serif;letter-spacing:.16em;text-transform:uppercase;margin:10px 0 6px}
footer .tels span:first-child{margin-top:0}
footer .tels a{display:block;white-space:nowrap;line-height:1.8}
.oui-non{display:grid;grid-template-columns:1fr 1fr;gap:26px}
.colonne{border-radius:4px;padding:34px 36px}
.colonne h3{display:flex;align-items:center;gap:14px;font-size:30px;margin-bottom:12px}
.colonne h3 i{width:36px;height:36px;border-radius:50%;display:grid;place-items:center;font:700 17px/1 Manrope,sans-serif;font-style:normal;flex-shrink:0}
.colonne ul{list-style:none}
.colonne li{padding:18px 0;border-top:1px solid rgba(244,239,228,.16);display:flex;justify-content:space-between;align-items:baseline;gap:24px}
.colonne li b{font-family:"Cormorant Garamond",serif;font-size:25px;font-weight:500}
.colonne li span{font:600 11px/1.6 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;text-align:right}
.colonne.oui{background:rgba(244,239,228,.07);border:1px solid rgba(200,154,58,.45)}
.colonne.oui h3 i{background:var(--or);color:var(--vert)}
.colonne.oui li span{color:var(--or)}
.colonne.non{background:#2A1E16;border:1px solid rgba(214,140,108,.35)}
.colonne.non h3{color:#F0C9B6}
.colonne.non h3 i{background:#B4553A;color:#FBEDE5}
.colonne.non li b{color:rgba(244,239,228,.72)}
.colonne.non li b:before{content:"✕";font:700 13px/1 Manrope,sans-serif;color:#D98B6C;margin-right:12px;position:relative;top:-3px}
.colonne.non li span{color:#D98B6C}
.bloc-plein{padding:0}
.bloc-plein .deux{gap:0;align-items:stretch}
.bloc-plein .photo{height:auto;min-height:620px;border-radius:0}
.bloc-texte{padding:100px}
.bloc-texte h2{color:var(--creme);font-size:54px}
.bloc-texte h2 em{color:var(--or)}
.bloc-texte p{color:rgba(244,239,228,.82)}
h2.citation{color:var(--creme);font-size:44px;line-height:1.2}
h2.citation em{color:var(--or)}
.encre .deux h2{color:var(--creme)}.encre .deux h2 em{color:var(--or)}.encre .deux p{color:rgba(244,239,228,.82)}
.faits.clair{border-color:var(--trait)}.faits.clair b{color:var(--terre)}.faits.clair span{color:var(--encre2)}
.points{display:none}

/* ---- nav : paliers intermédiaires, rien ne se chevauche ---- */
@media (max-width:1480px){nav,nav.colle{padding-left:48px;padding-right:48px}nav ul{gap:26px}nav .droite{gap:16px}nav .lang{margin-left:0}}
@media (max-width:1300px){
  nav,nav.colle{padding-left:30px;padding-right:30px}nav ul,nav .cta{display:none}nav .burger{display:block}nav .droite{gap:10px}
  nav.colle .cta{display:none}
  nav.ouvert{background:var(--vert)!important;color:var(--creme)!important}
  nav.ouvert ul{display:flex;flex-direction:column;gap:0;position:fixed;inset:0;overflow-y:auto;background:var(--vert);padding:108px 30px calc(34px + env(safe-area-inset-bottom,0px));z-index:19;white-space:normal;font:500 30px/1.1 "Cormorant Garamond",serif;letter-spacing:0}
  nav.ouvert ul li{border-bottom:1px solid rgba(244,239,228,.14)}
  nav.ouvert ul li a{display:block;padding:18px 0;color:var(--creme);border:0}
  nav.ouvert ul li a.ici{color:var(--or)}
  nav.ouvert .menu-plus{display:block;border:0;margin-top:14px}
  nav.ouvert .menu-plus:first-of-type{margin-top:30px}
  nav.ouvert .menu-plus a{display:flex;padding:18px;font:600 13px/1 Manrope,sans-serif;letter-spacing:.12em;text-transform:uppercase;text-align:center;justify-content:center}
  nav.ouvert .menu-plus a.or{color:var(--vert)}
  nav.ouvert .logo,nav.ouvert .droite{position:relative;z-index:20}
  nav.ouvert .logo b,nav.ouvert .lang,nav.ouvert .burger{color:var(--creme)!important;border-color:rgba(244,239,228,.45)!important}
  html.menu-ouvert{overflow:hidden}html.menu-ouvert .barre-action{display:none}
  /* une nav collante porte transform et backdrop-filter : le panneau fixe se calait sur elle au lieu de l'écran */
  nav.ouvert,nav.ouvert.colle{transform:none!important;backdrop-filter:none!important;-webkit-backdrop-filter:none!important;transition:none!important}
}

/* ================================================================
   MOBILE FIRST (≤ 1100 px) : une colonne, pouces, cartes à balayer
   ================================================================ */
@media (max-width:1100px){
  :root{--g:24px}
  body{font-size:16px;line-height:1.62;padding-bottom:84px}
  .wrap{width:calc(100% - 2*var(--g))}
  section{padding:64px 0}section.serre{padding:48px 0}
  [data-reveal]{transform:translateY(16px)}
  .wa-flottant{display:none}

  /* navigation */
  nav{padding:14px var(--g)}nav.colle{padding:10px var(--g)}
  nav ul,nav .cta{display:none}nav .burger{display:block;height:44px;min-width:76px;padding:0 14px}nav .droite{gap:10px}
  nav .lang{display:grid;place-items:center;height:44px;min-width:48px;padding:0 12px;margin:0}
  nav .logo b{font-size:21px;letter-spacing:.18em}

  /* héros : plein écran, texte en bas, boutons au pouce */
  .hero{min-height:88vh;min-height:88svh}
  .hero.court{min-height:64vh;min-height:64svh}
  .hero .voile,.hero .voile.bas{background:linear-gradient(180deg,rgba(9,30,23,.30) 0%,rgba(9,30,23,.45) 38%,rgba(9,30,23,.94) 100%)}
  .hero .txt{padding:0 var(--g) 40px;width:100%}
  .hero h1,.hero.court h1{font-size:42px;line-height:1.04;margin:0 0 16px}
  .une-ligne{white-space:normal}
  .hero p{font-size:16.5px;max-width:none}
  .hero .actions{flex-direction:column;gap:10px;margin-top:26px}
  .hero .actions .btn{width:100%;text-align:center;padding:18px 20px;font-size:12.5px}

  /* titres et intros */
  .tete{flex-direction:column;align-items:flex-start;gap:14px;margin-bottom:30px}
  .tete h2,.deux h2{font-size:36px;line-height:1.08;margin:0 0 14px}
  .tete p{max-width:none;font-size:16px}
  .manifeste p{font-size:26px;line-height:1.3}
  h2.citation,.bloc-texte h2{font-size:30px}

  /* deux colonnes → une colonne, image d'abord et pleine largeur */
  .deux{grid-template-columns:1fr;gap:30px}
  .deux>.photo,.deux>.carte-svg{order:-1}
  .deux>.photo{margin:0 calc(-1*var(--g));border-radius:0;height:auto!important;aspect-ratio:4/3}
  section>.wrap.deux>.photo{margin-top:-64px}section.serre>.wrap.deux>.photo{margin-top:-48px}
  .photo>img{top:0;height:100%}
  .bloc-plein .deux{gap:0}.bloc-plein .photo{min-height:0;aspect-ratio:4/3;margin:0}
  .bloc-texte{padding:40px var(--g) 56px}
  .carte-svg{padding:18px}

  /* cartes à balayer : étapes, publics, chronologie, produits */
  .etapes,.publics,.chrono ol,.grille3,.produits .defile{display:flex!important;overflow-x:auto;scroll-snap-type:x mandatory;gap:14px;margin:0 calc(-1*var(--g));padding:4px var(--g) 8px;scroll-padding:0 var(--g);scrollbar-width:none;-webkit-overflow-scrolling:touch}
  .etapes::-webkit-scrollbar,.publics::-webkit-scrollbar,.chrono ol::-webkit-scrollbar,.grille3::-webkit-scrollbar,.produits .defile::-webkit-scrollbar{display:none}
  .etapes>.etape,.publics>.public,.chrono ol>li,.grille3>.card{flex:0 0 84%;scroll-snap-align:start}
  .etape .photo{height:auto;aspect-ratio:4/5;margin:0}
  .etape h3{font-size:26px}.etape .n{margin:16px 0 6px}
  .public{min-height:0;padding:26px 22px}
  .chrono{margin-top:10px}.chrono:before{display:none}
  .chrono ol>li{flex-basis:72%;background:var(--creme2);border-radius:4px;padding:24px 20px}
  .chrono li:before{display:none}
  .grille3>.card{min-height:440px}
  .points{display:flex;justify-content:center;gap:8px;margin-top:14px}
  .points i{width:7px;height:7px;border-radius:50%;background:var(--trait);transition:width .25s,background .25s}
  .points i.on{width:22px;border-radius:4px;background:var(--terre)}
  .sombre .points i{background:rgba(244,239,228,.25)}.sombre .points i.on{background:var(--or)}
  .etapes,.publics,.chrono ol,.grille3,.produits .defile{padding-top:10px;padding-bottom:30px}
  .points{margin-top:0}
  .etapes>.etape,.publics>.public,.chrono ol>li,.grille3>.card,.produits .defile>.rangee{border-radius:20px;overflow:hidden;box-shadow:0 18px 36px -18px rgba(14,46,36,.42),0 2px 6px rgba(14,46,36,.06)}
  .sombre .etapes>.etape,.sombre .publics>.public,.sombre .chrono ol>li,.sombre .grille3>.card,.encre .publics>.public{box-shadow:0 20px 40px -18px rgba(0,0,0,.7),0 2px 6px rgba(0,0,0,.2)}
  .etapes>.etape{background:var(--creme2);padding-bottom:24px}
  .sombre .etapes>.etape{background:#16392E}
  .etapes>.etape>*:not(.photo){padding:0 22px}
  .etape .photo{border-radius:0}
  .publics>.public{background:rgba(244,239,228,.07);border-color:rgba(244,239,228,.16)}
  .chrono ol>li{border-radius:20px}
  .grille3>.card .cap{padding-left:24px;padding-right:24px}
  .carrousel>*{transition:transform .5s cubic-bezier(.2,.7,.2,1),opacity .5s,box-shadow .5s!important;transition-delay:0s!important;will-change:transform}
  .carrousel>:not(.actif),.carrousel>.vu:not(.actif){transform:scale(.94);opacity:.7}
  .carrousel>.actif:active{transform:scale(.98)}
  .carrousel>.card.actif img{animation:respire 9s ease-in-out infinite alternate}
  @keyframes respire{from{transform:scale(1)}to{transform:scale(1.06)}}
  @media (prefers-reduced-motion:reduce){.carrousel>*,.carrousel>:not(.actif),.carrousel>.vu:not(.actif){transform:none;opacity:1;transition:none!important}.carrousel>.card.actif img{animation:none}}
  .indice{display:block;font:500 11px/1 Manrope,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--encre2);margin:0 0 14px}

  /* listes : libellé au-dessus, valeur dessous */
  .liste li{flex-direction:column;align-items:flex-start;gap:6px;padding:16px 0}
  .liste li b{font-size:23px}
  .liste li span{text-align:left;max-width:none}
  .oui-non{grid-template-columns:1fr;gap:16px}
  .colonne{padding:24px 20px}.colonne h3{font-size:25px}
  .colonne li{flex-direction:column;gap:4px;padding:14px 0}.colonne li span{text-align:left}
  .faits{gap:18px 20px;margin-top:28px;padding-top:22px}.faits b{font-size:34px}

  /* produits */
  .autres{display:grid;grid-template-columns:1fr 1fr;border:0;gap:8px}
  .autres a{border:1px solid var(--trait)!important;border-radius:4px;padding:16px 8px}
  .produits{grid-template-columns:1fr;gap:18px}
  .produits .index{display:flex;gap:8px;overflow-x:auto;padding:10px var(--g);margin:0 calc(-1*var(--g));position:sticky;top:0;background:var(--creme);z-index:5;scrollbar-width:none}
  .produits .index::-webkit-scrollbar{display:none}
  .produits .index a{flex:0 0 auto;border:1px solid var(--trait)!important;border-radius:999px;padding:10px 16px;font-size:17px;min-height:44px;display:flex;align-items:center}
  .produits .index a.actif{background:var(--vert);color:var(--creme);border-color:var(--vert)!important;padding-left:16px}
  .produits .index a span{display:none}
  .rangee{flex:0 0 86%;scroll-snap-align:start;display:flex;flex-direction:column;gap:0;padding:0;border:0;background:var(--creme2);border-radius:20px;overflow:hidden}
  .rangee .photo{width:100%;height:auto;aspect-ratio:4/3;border-radius:0;order:0}
  .rangee>*:not(.photo){padding:24px 20px}
  .rangee .photo{align-self:stretch;flex:1 0 auto}
  .rangee>*:not(.photo){flex:0 0 auto}
  .rangee h2{font-size:32px}
  .rangee .mini{grid-template-columns:1fr;gap:0;margin:20px 0 22px;padding-top:0;border-top:0}
  .rangee .mini>div{display:flex;align-items:baseline;justify-content:space-between;gap:18px;padding:11px 0;border-top:1px solid var(--trait)}
  .rangee .mini span{flex:0 0 auto}
  .rangee .mini b{text-align:right}

  /* fiche produit : tuiles */
  .fiche{grid-template-columns:1fr 1fr;gap:8px;border:0}
  .fiche div{display:block;padding:14px;border:0!important;background:var(--creme2);border-radius:4px}
  .fiche div:nth-child(odd),.fiche div:nth-child(even){padding:14px}
  .fiche span{display:block;margin-bottom:6px}
  .fiche b{font-size:20px}

  /* formulaires : gros champs, pas de zoom iOS */
  .form{padding:26px 20px}
  .form input,.form select,.form textarea{font-size:16px;padding:14px 0}
  .form .btn{width:100%;padding:19px;font-size:12.5px}
  .form h3{font-size:26px}

  /* FAQ, cartes */
  .faq summary{font-size:22px;padding:18px 0}
  .card .cap{padding:60px 20px 20px}

  /* pied de page */
  footer{padding:52px 0 30px}
  footer .wrap{grid-template-columns:1fr 1fr;gap:34px 24px}
  footer .wrap>div:first-child{grid-column:1/-1}
  footer ul li a{display:inline-block;padding:4px 0}
  footer .bas{flex-direction:column;gap:8px}

  /* barre d'action fixe */
  .barre-action{position:fixed;left:0;right:0;bottom:0;z-index:25;display:flex;gap:10px;padding:10px 14px calc(10px + env(safe-area-inset-bottom,0px));background:rgba(244,239,228,.97);border-top:1px solid var(--trait);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px)}
  .barre-action a{flex:1;text-align:center;padding:16px 8px;font-size:12px;display:flex;align-items:center;justify-content:center;gap:8px;min-height:52px}
  .barre-action a.wa{flex:0 0 38%}
}
@media (max-width:640px){
  :root{--g:20px}
  .hero h1,.hero.court h1{font-size:37px}
  .tete h2,.deux h2{font-size:32px}
  .manifeste p{font-size:23px}
  footer .wrap{grid-template-columns:1fr}
  .fiche b{font-size:18px}
  .mention{font-size:8.5px;letter-spacing:.06em;padding:7px 10px}
}
"""

# ---------------------------------------------------------------- JS
JS = r"""
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
"""


# ---------------------------------------------------------------- SEO
SITE_URL = "https://taspalm.com"   # domaine détenu par l agence, confirmé par Yann le 17/09/2026
ALT = {
 "reel-cacao-ouvert.jpg":"Cabosse de cacao ouverte, fèves fraîches dans leur pulpe blanche, et cabosses entières sur des feuilles, photographie d'avril 2025",
 "reel-cacao-cabosses.jpg":"Cabosses de cacao récoltées, posées sur une table de bois, photographie d'avril 2025",
 "reel-cacao-arbre.jpg":"Cabosses de cacao vertes sur le tronc d'un cacaoyer du domaine, photographie d'avril 2025",
 "reel-cacao-feves.jpg":"Fèves de cacao étalées pour le séchage, photographie d'avril 2025",
 "reel-cacaoyers.jpg":"Cacaoyers en production sous les palmiers à huile, photographie d'avril 2025",
 "reel-fermentation.jpg":"Caisses en bois utilisées pour le miel, photographie d'avril 2025",
 "reel-sechage.jpg":"Claies de séchage du cacao sous les palmiers, photographie d'avril 2025",
 "reel-regime.jpg":"Régimes de noix de palme fraîchement coupés, photographie d'avril 2025",
 "reel-noix-palme.jpg":"Noix de palme rouges et orange détachées du régime, photographie d'avril 2025",
 "reel-ruche.jpg":"Ruche en bois avec ses abeilles à l'entrée, en lisière de la plantation, photographie d'avril 2025",
 "reel-ruche-arbre.jpg":"Ruche installée sous un arbre du domaine, photographie d'avril 2025",
 "reel-ananas-pied.jpg":"Ananas sur pied dans le champ, photographie d'avril 2025",
 "reel-ananas-champ.jpg":"Champ d'ananas du domaine au lever du jour, photographie d'avril 2025",
 "reel-corossol.jpg":"Corossols entiers et corossol coupé sur des feuilles, photographie d'avril 2025",
 "reel-corossol-arbre.jpg":"Corossols sur l'arbre, photographie d'avril 2025",
 "reel-pepiniere-cacao.jpg":"Pépinière de jeunes cacaoyers en sachets, photographie d'avril 2025",
 "reel-pepiniere-palmiers.jpg":"Jeunes palmiers à huile en pépinière, photographie d'avril 2025",
 "reel-piste.jpg":"Arbres fruitiers, jeunes ananas et palmiers le long de la piste du domaine, photographie d'avril 2025",
 "reel-palmiers-2025.jpg":"Palmiers à huile adultes du domaine, photographie d'avril 2025",
 "reel-cacao-jeune.jpg":"Jeune cacaoyer planté sous les palmiers, photographie d'avril 2025",
 "reel-sechage-feves.jpg":"Fèves de cacao en cours de séchage sur des claies en bois, sous les palmiers du domaine",
 "reel-sechage-feves-2.jpg":"Claies couvertes de fèves de cacao au séchage, devant les palmiers à huile",
 "reel-riviere.jpg":"La rivière bordée de forêt, vue depuis la berge, photographie de janvier 2018",
 "reel-riviere-portrait.jpg":"La rivière et sa berge herbeuse, photographie de janvier 2018",
 "reel-village.jpg":"Village de la Likouala : cases aux toits de chaume, piste de terre et bananiers, photographie de janvier 2018",
 "reel-confluence.jpg":"Confluence de deux rivières vue du ciel, près du domaine, photographie de septembre 2021",
 "reel-barge.jpg":"Barges à quai sur la rivière, vue du ciel, photographie de septembre 2021",
 "reel-palmiers.jpg":"Palmiers à huile du domaine Taspalm, photographie d'avril 2022",
 "reel-palmiers-ciel.jpg":"Piste et palmiers à huile du domaine vus du ciel, photographie d'avril 2022",
 "reel-pepiniere.jpg":"Pépinière de jeunes palmiers sous ombrière, photographie d'avril 2022",
 "reel-pepiniere-sacs.jpg":"Jeunes plants en sachets à la pépinière, photographie d'avril 2022",
 "reel-miel.jpg":"Rayon de miel du domaine sur une assiette, photographie d'avril 2022",
 "reel-ananas.jpg":"Ananas récoltés sur le domaine, photographie d'août 2022",
 "reel-aubergines.jpg":"Aubergine sur pied dans les cultures vivrières du domaine, photographie d'avril 2022",
 "reel-plantation-jeune.jpg":"Jeunes plantations tuteurées sur le domaine, photographie d'avril 2022",
 "hero-domaine-1600.jpg":"Vue aérienne du domaine Taspalm à Ibenga : palmiers à huile, arbres fruitiers et cultures vivrières, photographie prise en avril 2022",
 "hero-domaine-800.jpg":"Vue aérienne du domaine Taspalm à Ibenga, photographie prise en avril 2022",
 "A-hero.jpg":"Nature morte de noix de palme, cabosses de cacao ouvertes, safous et pot d'huile sur un lin brun, image d'illustration",
 "A-huile.jpg":"Bouteille d'huile de palme rouge à côté de noix de palme et d'une palme, image d'illustration",
 "A-cacao.jpg":"Cabosses de cacao jaunes et rouges sur le tronc d'un cacaoyer, image d'illustration",
 "A-safou.jpg":"Safous violets mûrs posés sur une feuille de bananier, image d'illustration",
 "A-miel.jpg":"Pot de miel doré, rayon de miel et cuillère en bois, image d'illustration",
 "A-ananas.jpg":"Ananas entier et ananas coupé sur un lin brun, image d'illustration",
 "A-mais.jpg":"Épis de maïs jaune partiellement déshabillés, image d'illustration",
 "A-legumes.jpg":"Aubergines africaines, gombos, piments et feuilles de manioc, image d'illustration",
 "A-regime.jpg":"Régime de noix de palme rouge accroché au tronc d'un palmier à huile, image d'illustration",
 "A-pressoir.jpg":"Atelier de pressage artisanal d'huile de palme avec bassines d'huile rouge, image d'illustration",
 "A-fermentation.jpg":"Caisses de fermentation en bois remplies de fèves de cacao sous feuilles de bananier, image d'illustration",
 "A-village.jpg":"Village au bord d'une rivière brune en Afrique centrale, cases et pirogues dans la brume du matin, image d'illustration",
 "A-foret.jpg":"Sous-bois de forêt équatoriale traversé de rayons de lumière, image d'illustration",
 "A-safoutier.jpg":"Grappes de safous violets sur les branches d'un safoutier, image d'illustration",
 "A-pirogue.jpg":"Pirogue chargée de sacs et de bidons amarrée sur la rive d'une rivière, image d'illustration",
 "B-aerien.jpg":"Vue aérienne de rangées de palmiers à huile à la confluence de deux rivières bordées de forêt, image d'illustration",
 "B-sechage.jpg":"Aire de séchage de fèves de cacao sur claies devant un bâtiment agricole, image d'illustration",
 "C-riviere.jpg":"Pirogue en bois sur la rive d'une large rivière brune à l'heure bleue, image d'illustration",
 "C-portrait.jpg":"Portrait d'une agricultrice dans une plantation de palmiers, image d'illustration",
 "C-abeilles.jpg":"Ruche en bois dans une clairière tropicale avec des abeilles en vol, image d'illustration",
}
def alt(img): return ALT.get(img, "")
TITRES = {
 "index.html":"Taspalm · Huile de palme, cacao et safou de la Likouala, Congo",
 "l-exploitation.html":"L'exploitation Taspalm, à Ibenga depuis 2006",
 "produits.html":"Nos produits · huile de palme, cacao, safou, miel, ananas, maïs, légumes",
 "huile-de-palme.html":"Huile de palme rouge de la Likouala, pressée sur place",
 "cacao.html":"Cacao d'Ibenga, fermenté et séché au soleil",
 "safou.html":"Safou, le fruit violet de la Likouala",
 "terroir.html":"Le terroir · Ibenga, Enyellé, Likouala, entre l'Ibenga et l'Oubangui",
 "professionnels.html":"Professionnels · acheter, transformer, distribuer avec Taspalm",
 "visiter.html":"Visiter l'exploitation à Ibenga, Likouala",
 "contact.html":"Contact · écrire à Taspalm, Congo et Europe",
 "mentions-legales.html":"Mentions légales",
 "confidentialite.html":"Confidentialité",
 "merci.html":"Message envoyé · Taspalm",
}
DESC = {
 "index.html":"Taspalm, exploitation agricole à Ibenga (Likouala, Congo) depuis 2006 : huile de palme, cacao, safou, miel, ananas, maïs et légumes, vendus en direct.",
 "l-exploitation.html":"Une exploitation agricole fondée en 2006 à Ibenga, district d'Enyellé, Likouala. Ce que nous faisons, ce que nous ne faisons pas, et les gestes de la saison.",
 "produits.html":"Sept cultures sur une même terre : huile de palme, cacao, safou, miel, ananas, maïs et légumes. Origine, saison et conditionnement de chaque produit.",
 "huile-de-palme.html":"Huile de palme rouge non raffinée, extraite des régimes du domaine Taspalm à Ibenga dans les jours qui suivent la récolte. Bidons, fûts et détail.",
 "cacao.html":"Fèves de cacao d'Ibenga, Likouala : cabosses ouvertes le jour de la récolte, fèves fermentées puis séchées sur claies. Pour chocolatiers et transformateurs.",
 "safou.html":"Le safou de la Likouala, cueilli mûr : frais en saison, transformé le reste de l'année. Un fruit d'Afrique centrale proposé par l'exploitation Taspalm.",
 "terroir.html":"Le domaine Taspalm est à Ibenga, district d'Enyellé, Likouala, à la confluence de l'Ibenga et de l'Oubangui. Sol, ombre, eau et façon de cultiver.",
 "professionnels.html":"Distributeurs, transformateurs, restauration, investisseurs : quatre façons de travailler avec l'exploitation Taspalm, en direct, à partir de votre besoin.",
 "visiter.html":"Venir à Ibenga : une journée sur l'exploitation, du palmier au pressoir. Visites, immersions et formations, accès depuis Impfondo.",
 "contact.html":"Écrire ou appeler Taspalm : coordonnées au Congo et en Europe, adresse du domaine à Ibenga, Likouala.",
 "mentions-legales.html":"Mentions légales du site Taspalm.",
 "confidentialite.html":"Politique de confidentialité du site Taspalm : aucun traceur, polices hébergées sur le site, et ce que deviennent les messages envoyés depuis le site.",
}
HERO_IMG = {"index.html":"hero-domaine-1600.jpg","l-exploitation.html":"reel-palmiers-ciel.jpg","produits.html":"reel-cacao-cabosses.jpg","huile-de-palme.html":"A-huile.jpg","cacao.html":"reel-cacao-cabosses.jpg","safou.html":"A-safoutier.jpg","terroir.html":"hero-domaine-1600.jpg","professionnels.html":"reel-barge.jpg","visiter.html":"reel-riviere.jpg","contact.html":"reel-palmiers.jpg","mentions-legales.html":"reel-palmiers.jpg","confidentialite.html":"reel-palmiers.jpg","merci.html":"reel-palmiers.jpg"}
FIL = {"l-exploitation.html":"L'exploitation","produits.html":"Nos produits","huile-de-palme.html":("Nos produits","produits.html","Huile de palme"),"cacao.html":("Nos produits","produits.html","Cacao"),"safou.html":("Nos produits","produits.html","Safou"),"terroir.html":"Le terroir","professionnels.html":"Professionnels","visiter.html":"Visiter","contact.html":"Contact","mentions-legales.html":"Mentions légales","confidentialite.html":"Confidentialité"}
import json
ORG = {"@type":"Organization","@id":SITE_URL+"/#organisation","name":"Taspalm","url":SITE_URL+"/","logo":SITE_URL+"/favicon.svg","foundingDate":"2006",
       "description":"Exploitation agricole à Ibenga, district d'Enyellé, département de la Likouala, République du Congo.",
       "address":{"@type":"PostalAddress","addressLocality":"Ibenga","addressRegion":"Likouala","addressCountry":"CG"},
       "telephone":["+242055361605","+242069932364","+33780735382","+33649106650"],
       "areaServed":["CG","FR"]}
def jsonld(fichier, lang="fr"):
    tx=(lambda x:x) if lang=="fr" else tr
    g=[dict(ORG, description=tx(ORG["description"])),{"@type":"WebSite","@id":SITE_URL+"/#site","url":SITE_URL+"/","name":"Taspalm","inLanguage":lang,"publisher":{"@id":SITE_URL+"/#organisation"}}]
    fil=FIL.get(fichier)
    if fil:
        base=SITE_URL+("/" if lang=="fr" else "/en/"); items=[{"@type":"ListItem","position":1,"name":tx("Accueil"),"item":base}]
        if isinstance(fil,tuple):
            items.append({"@type":"ListItem","position":2,"name":tx(fil[0]),"item":base+fil[1]}); items.append({"@type":"ListItem","position":3,"name":tx(fil[2]),"item":base+fichier})
        else: items.append({"@type":"ListItem","position":2,"name":tx(fil),"item":base+fichier})
        g.append({"@type":"BreadcrumbList","itemListElement":items})
    PROD={"huile-de-palme.html":("Huile de palme rouge Taspalm","Huile de palme brute non raffinée, pressée sur place à Ibenga, Likouala.","Huile végétale"),
          "cacao.html":("Cacao Taspalm, fèves séchées","Fèves de cacao fermentées puis séchées sur claies, origine Ibenga, Likouala.","Cacao"),
          "safou.html":("Safou Taspalm","Safou frais en saison et transformé hors saison, cueilli mûr à Ibenga, Likouala.","Fruit")}
    if fichier in PROD:
        n,d,c=PROD[fichier]
        g.append({"@type":"Product","name":tx(n),"description":tx(d),"category":tx(c),"image":SITE_URL+"/images/"+HERO_IMG[fichier],"brand":{"@type":"Brand","name":"Taspalm"},"manufacturer":{"@id":SITE_URL+"/#organisation"},"countryOfOrigin":"CG"})
    return json.dumps({"@context":"https://schema.org","@graph":g},ensure_ascii=False)


# ---------------------------------------------------------------- traduction (site miroir /en/)
import importlib.util as _ilu
_sp=_ilu.spec_from_file_location("traductions_en", os.path.join(B,"traductions_en.py")); _m=_ilu.module_from_spec(_sp)
try: _sp.loader.exec_module(_m); TX=_m.TX; TITRES_EN=_m.TITRES_EN; DESC_EN=_m.DESC_EN
except FileNotFoundError: TX={}; TITRES_EN={}; DESC_EN={}
MANQUANTS=set()
DEJA_EN=set(TX.values())|set(TITRES_EN.values())|set(DESC_EN.values())
def _traduisible(t):
    return bool(re.search(r"[A-Za-zÀ-ÿ]", t)) and not t.startswith("{") and not re.fullmatch(r"[\d\s+·/%.,:()xX-]*", t)
def tr(t):
    st=t.strip()
    if not _traduisible(st): return t
    if st in DEJA_EN: return t
    e=TX.get(st)
    if e is None: MANQUANTS.add(st); return t
    return t.replace(st, e)
def traduire(h):
    h=re.sub(r">([^<>]+)<", lambda m: ">"+tr(m.group(1))+"<", h)
    h=re.sub(r'\b(alt|aria-label|placeholder|data-fermer|data-menu|title)="([^"]*)"', lambda m: '%s="%s"' % (m.group(1), tr(m.group(2))), h)
    return h

WA_FR = 'https://wa.me/242069932364?text=Bonjour%20Taspalm%2C%20'
WA_EN = 'https://wa.me/242069932364?text=Hello%20Taspalm%2C%20'
ICO_WA = '<svg class="ico-wa" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M12 2.2a9.8 9.8 0 0 0-8.4 14.8L2.3 21.8l4.9-1.3A9.8 9.8 0 1 0 12 2.2zm0 1.8a8 8 0 1 1-4.1 14.9l-.3-.2-2.9.8.8-2.8-.2-.3A8 8 0 0 1 12 4zm-3.1 3.9c-.2 0-.5 0-.7.3-.2.3-.9.9-.9 2.2s.9 2.5 1 2.7c.1.2 1.8 2.9 4.5 3.9 2.2.9 2.7.7 3.2.7.5-.1 1.5-.6 1.7-1.2.2-.6.2-1.1.2-1.2-.1-.1-.3-.2-.6-.3l-1.9-.9c-.3-.1-.5-.1-.7.2-.2.3-.7.9-.9 1.1-.2.2-.3.2-.6.1-.3-.1-1.1-.4-2.1-1.3-.8-.7-1.3-1.5-1.5-1.8-.2-.3 0-.4.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.1c-.2-.5-.4-.5-.6-.5h-.6z"/></svg>'

# ---------------------------------------------------------------- gabarit
NAV = [("l-exploitation.html","L'exploitation"),("produits.html","Nos produits"),("terroir.html","Le terroir"),("professionnels.html","Professionnels"),("visiter.html","Visiter")]

def nav(actif, lang="fr", fichier="index.html"):
    li = "".join('<li><a href="%s"%s>%s</a></li>' % (h, ' class="ici"' if h == actif else "", t) for h, t in NAV)
    autre = ('<a class="lang" href="en/%s" hreflang="en" lang="en" aria-label="English version">EN</a>' % fichier) if lang=="fr" else ('<a class="lang" href="../%s" hreflang="fr" lang="fr" aria-label="Version française">FR</a>' % fichier)
    li += ('<li class="menu-plus"><a class="btn or" href="professionnels.html#besoin">Exprimez votre besoin</a></li>'
           '<li class="menu-plus"><a class="btn wa" href="%s" target="_blank" rel="noopener">%sDiscuter sur WhatsApp</a></li>') % (WA_FR, ICO_WA)
    return ('<nav aria-label="Navigation principale"><a class="logo" href="index.html"><b>TASPALM</b></a>'
            '<ul>%s</ul><div class="droite">%s<a class="cta" href="professionnels.html#besoin">Exprimez votre besoin</a>'
            '<button class="burger" aria-label="Menu" aria-expanded="false" data-fermer="Fermer">Menu</button></div></nav>') % (li, autre)

FOOTER = """<footer><div class="wrap">
  <div><b>TASPALM</b><p>Exploitation agricole, Ibenga, district d'Enyellé, département de la Likouala, République du Congo. Fondée en 2006.</p>
    <p style="margin-top:14px"><a class="lien clair" href="contact.html">Écrire à l'exploitation</a></p></div>
  <div><span class="sur">L'exploitation</span><ul><li><a href="l-exploitation.html">Qui nous sommes</a></li><li><a href="terroir.html">Le terroir</a></li><li><a href="visiter.html">Venir à Ibenga</a></li><li><a href="contact.html">Contact</a></li></ul></div>
  <div><span class="sur">Nos produits</span><ul><li><a href="huile-de-palme.html">Huile de palme</a></li><li><a href="cacao.html">Cacao</a></li><li><a href="safou.html">Safou</a></li><li><a href="produits.html">Miel, ananas, maïs, légumes</a></li></ul></div>
  <div><span class="sur">Professionnels</span><ul><li><a href="professionnels.html">Acheter, transformer, distribuer</a></li><li><a href="professionnels.html#besoin">Exprimez votre besoin</a></li><li><a href="__WA__" target="_blank" rel="noopener">Discuter sur WhatsApp</a></li></ul>
    <span class="sur" style="margin-top:22px">Téléphones</span><p class="tels"><span>Congo</span><a href="tel:+242055361605">+242 05 536 16 05</a><a href="tel:+242069932364">+242 06 993 23 64</a><span>Europe</span><a href="tel:+33780735382">+33 7 80 73 53 82</a><a href="tel:+33649106650">+33 6 49 10 66 50</a></p></div>
</div><div class="wrap bas"><span>© Taspalm 2026</span><span><a href="mentions-legales.html">Mentions légales</a> · <a href="confidentialite.html">Confidentialité</a></span></div><div class="wrap" style="margin-top:18px;font-size:11.5px;color:rgba(244,239,228,.4)">Les photographies ont été prises sur place entre 2018 et 2025. Celles qui portent la mention « image d'illustration » sont des visuels provisoires. Les valeurs entre crochets sont en cours de validation.</div></footer>
<div class="barre-action"><a class="btn or" href="professionnels.html#besoin">Exprimez votre besoin</a><a class="btn wa" href="__WA__" target="_blank" rel="noopener">__ICO__WhatsApp</a></div>
<a class="wa-flottant" href="__WA__" target="_blank" rel="noopener" aria-label="Discuter sur WhatsApp">__ICO__<span>Discuter sur WhatsApp</span></a>
<script src="site.js"></script>"""
FOOTER = FOOTER.replace("__WA__", WA_FR).replace("__ICO__", ICO_WA)

PAGES=[]
def enlever_casquettes(h):
    """retire les lignes en capitales avant les titres et les fils d'Ariane des héros (pied de page conservé)"""
    avant, sep, apres = h.partition("<footer>")
    avant = re.sub(r'<div class="fil">.*?</div>\s*', "", avant, flags=re.S)
    avant = re.sub(r'<span class="sur"[^>]*>.*?</span>\s*', "", avant, flags=re.S)
    return avant + sep + apres

def page(fichier, titre, actif, corps, lang="fr"):
    if lang=="fr": PAGES.append((fichier, titre, actif, corps))
    t=(TITRES if lang=="fr" else TITRES_EN).get(fichier, titre+" · Taspalm"); d=(DESC if lang=="fr" else DESC_EN).get(fichier,"")
    pref = "" if lang=="fr" else "en/"
    url=SITE_URL+"/"+pref+("" if fichier=="index.html" else fichier)
    url_fr=SITE_URL+"/"+("" if fichier=="index.html" else fichier); url_en=SITE_URL+"/en/"+("" if fichier=="index.html" else fichier)
    robots="noindex,follow" if fichier in ("mentions-legales.html","confidentialite.html","merci.html") else "index,follow"
    html = """<!doctype html>
<html lang="%s">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%s</title>
<meta name="description" content="%s">
<meta name="robots" content="%s">
<link rel="canonical" href="%s">
<link rel="alternate" hreflang="fr" href="%s">
<link rel="alternate" hreflang="en" href="%s">
<link rel="alternate" hreflang="x-default" href="%s">
<meta property="og:type" content="website">
<meta property="og:locale" content="%s">
<meta property="og:site_name" content="Taspalm">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="%s">
<meta property="og:image" content="%s/images/%s">
<meta property="og:image:alt" content="%s">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0E2E24">
<link rel="icon" href="favicon.svg" type="image/svg+xml">
<link rel="preload" href="fonts/cormorant-garamond.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="fonts/manrope.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="styles.css">
<script type="application/ld+json">%s</script>
</head>
<body>
<header>
%s
</header>
<main id="contenu">
%s
</main>
%s
</body>
</html>""" % (lang, t, d.replace('"','&quot;'), robots, url, url_fr, url_en, url_fr, "fr_FR" if lang=="fr" else "en_GB", t, d.replace('"','&quot;'), url, SITE_URL, HERO_IMG.get(fichier,"A-hero.jpg"), alt(HERO_IMG.get(fichier,"A-hero.jpg")), jsonld(fichier, lang), nav(actif, lang, fichier), corps, FOOTER)
    html = enlever_casquettes(html)
    html = html.replace("__WA__", WA_FR).replace("__ICO__", ICO_WA)
    if lang=="en":
        html = re.sub(r'(property="og:image:alt" content=")([^"]*)"', lambda m: m.group(1)+tr(m.group(2))+'"', html)
        html = traduire(html)
        html = re.sub(r'(src|href)="(images/|styles\.css|site\.js|favicon\.svg|fonts/)', r'\1="../\2', html)
        html = html.replace(WA_FR, WA_EN).replace('action="envoyer.php"','action="../envoyer.php"').replace('name="langue" value="fr"','name="langue" value="en"')
        os.makedirs(os.path.join(WWW,"en"), exist_ok=True)
        open(os.path.join(WWW, "en", fichier), "w").write(html)
    else:
        open(os.path.join(WWW, fichier), "w").write(html)
    print("page", pref+fichier)

def hero(img, fil, h1, p, court=False, actions="", origine="", voile="", px="0.2"):
    if img == "hero-domaine-1600.jpg":
        balise = ('<picture><source media="(max-width:1100px)" type="image/webp" srcset="images/hero-domaine-800.webp">'
                  '<source media="(max-width:1100px)" srcset="images/hero-domaine-800.jpg">'
                  '<source type="image/webp" srcset="images/hero-domaine-1600.webp">'
                  '<img src="images/hero-domaine-1600.jpg" alt="%s" width="1600" height="900" fetchpriority="high" data-px="%s"></picture>') % (alt(img), px)
    else:
        balise = '<img src="images/%s" alt="%s" width="1024" height="1024" fetchpriority="high" data-px="%s">' % (img, alt(img), px)
    return """<section class="hero%s">
  %s
  <div class="voile%s"></div>
  <div class="txt titre-anim" data-px="-0.06">
    <div class="fil">%s</div>
    <h1>%s</h1>
    <p>%s</p>
    %s
  </div>%s
</section>""" % (" court" if court else "", balise, voile, fil, h1, p,
                 ('<div class="actions">%s</div>' % actions) if actions else "", origine)

def photo(img, px="0.14", leg="", h=None, extra=""):
    return '<div class="photo"%s%s><img src="images/%s" alt="%s" width="1024" height="1024" loading="lazy" decoding="async" data-px="%s">%s</div>' % (
        (' style="height:%s"' % h) if h else "", extra, img, alt(img), px, ('<div class="leg">%s</div>' % leg) if leg else "")

def besoin_form(titre="Exprimez votre besoin", intro="Produit, usage, volume, pays : quatre réponses suffisent pour que l'exploitation vous fasse une proposition.", id_="besoin"):
    return """<form class="form" id="%s" method="post" action="envoyer.php" accept-charset="UTF-8">
  <h3>%s</h3><p>%s</p>
  <input type="hidden" name="formulaire" value="besoin"><input type="hidden" name="langue" value="fr"><input type="hidden" name="page" value=""><input type="hidden" name="t" value=""><div class="pot" aria-hidden="true"><label>Ne pas remplir<input type="text" name="site_web" tabindex="-1" autocomplete="off"></label></div>
  <label for="f-prod">Le produit</label><select id="f-prod" name="produit"><option>Huile de palme</option><option>Cacao</option><option>Safou</option><option>Miel</option><option>Ananas</option><option>Maïs</option><option>Légumes</option><option>Plusieurs produits</option></select>
  <label for="f-usage">Votre usage</label><select id="f-usage" name="usage"><option>Revente</option><option>Transformation</option><option>Restauration</option><option>Consommation personnelle</option><option>Partenariat ou investissement</option><option>Autre</option></select>
  <label for="f-vol">Volume envisagé, par mois ou par saison</label><input id="f-vol" name="volume" type="text" maxlength="120">
  <label for="f-pays">Pays ou ville de livraison</label><input id="f-pays" name="pays" type="text" maxlength="120" autocomplete="country-name">
  <label for="f-mail">Email ou WhatsApp</label><input id="f-mail" name="contact" type="text" maxlength="160" required minlength="5">
  <button class="btn vert" type="submit">Envoyer mon besoin</button>
  <p class="note">Votre message est envoyé à l'exploitation et sert uniquement à vous répondre. <a href="confidentialite.html">Confidentialité</a></p>
</form>""" % (id_, titre, intro)
echantillon_form = besoin_form

# ================================================================ ACCUEIL
accueil = hero("hero-domaine-1600.jpg", "Ibenga · Likouala · Congo",
    "L'huile de palme,<br>le cacao et le safou<br><em>de la Likouala.</em>",
    "Sept cultures sur une même terre, à la confluence de l'Ibenga et de l'Oubangui. Récoltées, transformées et expédiées par l'exploitation qui les fait pousser depuis 2006.",
    actions='<a class="btn or" href="produits.html">Voir la collection</a><a class="btn ghost" href="terroir.html">Le terroir</a>', px="0.22")

bande_items = "".join("<span>%s</span><span>·</span>" % s for s in ["Huile de palme","Cacao","Safou","Miel","Ananas","Maïs","Légumes"])
accueil += '<div class="bande"><div class="piste" data-pxx="0.08">%s%s</div></div>' % (bande_items, bande_items)

accueil += """<section><div class="wrap">
  <div class="tete" data-reveal>
    <h2>Trois produits <em>emblématiques,</em><br>quatre cultures de saison.</h2>
    <p>Chaque produit porte son origine, sa saison de récolte et son mode de transformation. Rien n'est acheté ailleurs pour être revendu.</p>
  </div>
  <span class="indice">Balayez pour voir les produits</span><div class="grille3">
    <a class="card" href="huile-de-palme.html" data-reveal><img src="images/A-huile.jpg" alt="Bouteille d'huile de palme rouge à côté de noix de palme et d'une palme, image d'illustration" width="1024" height="1024" loading="lazy" decoding="async"><div class="cap"><span class="sur">Pressée sur place</span><h3>Huile de palme</h3><p>Extraite dans les jours qui suivent la récolte. Conditionnements pro et détail.</p></div></a>
    <a class="card d2" href="cacao.html" data-reveal><img src="images/reel-cacao-ouvert.jpg" alt="Cabosse de cacao ouverte, fèves fraîches dans leur pulpe blanche, et cabosses entières sur des feuilles, photographie d'avril 2025" width="1024" height="1024" loading="lazy" decoding="async"><div class="cap"><span class="sur">Récolté à maturité</span><h3>Cacao</h3><p>Fèves fermentées et séchées sur claies. Pour transformateurs et chocolatiers.</p></div></a>
    <a class="card d3" href="safou.html" data-reveal><img src="images/A-safou.jpg" alt="Safous violets mûrs posés sur une feuille de bananier, image d'illustration" width="1024" height="1024" loading="lazy" decoding="async"><div class="cap"><span class="sur">Fruit de saison</span><h3>Safou</h3><p>Le fruit de la Likouala, cueilli mûr. Frais en saison, transformé le reste de l'année.</p></div></a>
  </div>
  <div class="autres d4" data-reveal>
    <a href="produits.html#miel"><b>Miel</b><span>Ruchers</span></a>
    <a href="produits.html#ananas"><b>Ananas</b><span>Récolté mûr</span></a>
    <a href="produits.html#mais"><b>Maïs</b><span>Céréale de base</span></a>
    <a href="produits.html#legumes"><b>Légumes</b><span>Frais, de saison</span></a>
  </div>
</div></section>"""

accueil += """<section class="sombre serre"><div class="wrap manifeste">
  <span class="sur" data-reveal>L'exploitation</span>
  <p data-reveal style="margin-top:22px">Nous ne sommes pas un négociant. Nous sommes <em>ceux qui plantent,</em> ceux qui récoltent, et ceux qui pressent.</p>
  <p class="d2" data-reveal>Ce que vous recevez a poussé ici, entre deux rivières, et n'a quitté Ibenga qu'une fois <em>prêt à voyager.</em></p>
  <p class="d3" data-reveal style="margin-top:34px"><a class="lien clair" href="l-exploitation.html">Qui nous sommes</a></p>
</div></section>"""

accueil += """<section><div class="wrap">
  <div class="tete" data-reveal><h2>De la récolte <em>au départ,</em><br>tout se fait ici.</h2><p>Deux récoltes, deux savoir-faire, un seul lieu : les régimes de noix de palme d'un côté, les fèves de cacao de l'autre.</p></div>
  <div class="etapes">
    <div class="etape" data-reveal>%s<div class="n">I</div><h3>Les régimes</h3><p>Les régimes de noix de palme sont coupés à maturité, quand les noix rougissent.</p></div>
    <div class="etape d2" data-reveal>%s<div class="n">II</div><h3>Les fèves</h3><p>Sorties des cabosses, les fèves de cacao sèchent au soleil sur des claies installées sous les palmiers.</p></div>
    <div class="etape d3" data-reveal>%s<div class="n">III</div><h3>Le départ</h3><p>Par la rivière ou par la route, vers Brazzaville, Pointe-Noire et l'export.</p></div>
  </div>
</div></section>""" % (photo("reel-regime.jpg","0.12","Régimes de noix de palme · avril 2025"), photo("reel-sechage-feves.jpg","0.12","Séchage des fèves de cacao sur claies"), photo("reel-barge.jpg","0.12","Barges à quai sur la rivière · septembre 2021"))

accueil += """<section class="sombre"><div class="wrap deux">
  <div data-reveal>
    <span class="sur">Le terroir</span>
    <h2>Une terre entre <em>deux rivières.</em></h2>
    <p>Le domaine est installé au village d'Ibenga, dans le district d'Enyellé, là où l'Ibenga rejoint l'Oubangui. Des cultures associées, à l'abri de la forêt.</p>
    <p>Depuis 2006, l'exploitation cultive, transforme sur place, et fait vivre les familles du village qui y travaillent.</p>
    <div class="faits">
      <div><b>2006</b><span>Année de fondation</span></div>
      <div><b>7</b><span>Cultures</span></div>
      <div><b>2</b><span>Rivières, l'Ibenga et l'Oubangui</span></div>
      <div><b>Sur place</b><span>Récolte et transformation</span></div>
    </div>
    <p style="margin-top:34px"><a class="lien clair" href="terroir.html">Découvrir le terroir</a></p>
  </div>
  %s
</div></section>""" % photo("reel-confluence.jpg","0.16","Confluence de deux rivières, vue du ciel · septembre 2021")

accueil += """<section><div class="wrap deux" style="align-items:start">
  <div data-reveal>
    <span class="sur">Professionnels</span>
    <h2>Acheter, transformer,<br><em>distribuer.</em></h2>
    <p>L'exploitation fournit en direct, sans intermédiaire. Chaque relation commence par un besoin clairement exprimé : dites-nous ce qu'il vous faut, nous vous répondons avec une proposition.</p>
    <ul class="liste">
      <li><b>Distributeurs et revendeurs</b><span>Détail et gros</span></li>
      <li><b>Transformateurs agroalimentaires</b><span>Matière première</span></li>
      <li><b>Restauration et hôtellerie</b><span>Approvisionnement</span></li>
      <li><b>Partenaires et investisseurs</b><span>Sur dossier</span></li>
    </ul>
    <p style="margin-top:30px"><a class="lien" href="professionnels.html">Tout sur les partenariats</a></p>
  </div>
  <div class="d2" data-reveal>%s</div>
</div></section>""" % echantillon_form()

accueil += """<section class="encre bloc-plein"><div class="deux">
  %s
  <div class="bloc-texte" data-reveal>
    <h2>Venir à Ibenga, <em>voir de ses yeux.</em></h2>
    <p>L'exploitation reçoit des visiteurs, des étudiants et des porteurs de projet. On marche dans la plantation, on assiste au pressage, on goûte. La page Visiter dit comment venir et où dormir.</p>
    <p style="margin-top:30px"><a class="btn or" href="visiter.html">Préparer une visite</a></p>
  </div>
</div></section>""" % photo("reel-riviere.jpg","0.14","La rivière, près de Dongou · janvier 2018")

page("index.html", "L'Exploitation", "", accueil)

# ================================================================ L'EXPLOITATION
maison = hero("reel-palmiers-ciel.jpg", "<a href=\"index.html\">Taspalm</a> · L'exploitation",
    "<span class=\"une-ligne\">Une exploitation agricole</span><br>à Ibenga, <em>depuis 2006.</em>",
    "Ce que nous sommes, ce que nous faisons, et ce que nous refusons de faire. Vingt saisons dans un seul village.", court=True, voile=" bas")

maison += """<section><div class="wrap manifeste">
  <span class="sur" data-reveal>Manifeste</span>
  <p data-reveal style="margin-top:22px">Nous plantons, nous récoltons, nous pressons, nous séchons. Puis nous chargeons la pirogue. <em>Tout ce qui porte notre nom est passé par nos mains.</em></p>
  <p class="d2" data-reveal>Nous ne promettons pas des tonnes que nous n'avons pas. Nous disons ce que la saison donne, et quand.</p>
</div></section>"""

maison += """<section class="sombre"><div class="wrap">
  <div class="tete" data-reveal><h2>Ce que nous faisons, <em>et pas.</em></h2><p>Ce que vous pouvez attendre de nous, et ce que vous n'obtiendrez pas.</p></div>
  <div class="oui-non">
    <div class="colonne oui" data-reveal><h3><i aria-hidden="true">✓</i>Ce que nous faisons</h3><ul>
      <li><b>Cultiver sept cultures</b><span>Palmier, cacao, safou, miel, ananas, maïs, légumes</span></li>
      <li><b>Transformer sur place</b><span>Huile, cacao, miel</span></li>
      <li><b>Vendre en direct</b><span>Sans intermédiaire</span></li>
      <li><b>Recevoir</b><span>Visites et formations</span></li>
    </ul></div>
    <div class="colonne non d2" data-reveal><h3><i aria-hidden="true">✕</i>Ce que nous ne faisons pas</h3><ul>
      <li><b>Acheter pour revendre</b><span>Rien ne vient d'ailleurs</span></li>
      <li><b>Promettre un volume sans récolte</b><span>La saison décide</span></li>
      <li><b>Mélanger les origines</b><span>Une terre, un nom</span></li>
      <li><b>Affirmer ce qu'on ne sait pas</b><span>On préfère le dire</span></li>
    </ul></div>
  </div>
</div></section>"""

maison += """<section><div class="wrap">
  <div class="tete" data-reveal><h2>Vingt ans, <em>en cinq dates.</em></h2><p>Seule la fondation est établie. Les autres jalons sont à fournir par l'exploitation, ils remplacent les emplacements ci-dessous.</p></div>
  <div class="chrono" data-reveal><ol>
    <li><b>2006</b><p>Fondation de l'exploitation à Ibenga, district d'Enyellé.</p></li>
    <li class="attente"><b>[ année ]</b><p>Premières plantations de cacao. Date et surface à fournir.</p></li>
    <li class="attente"><b>[ année ]</b><p>Mise en service de l'atelier de pressage. À confirmer.</p></li>
    <li class="attente"><b>[ année ]</b><p>Premiers ruchers, première récolte de miel. À confirmer.</p></li>
    <li class="attente"><b>[ année ]</b><p>Première expédition hors du département. Destination à fournir.</p></li>
  </ol></div>
</div></section>"""

maison += """<section class="serre" style="padding-top:0"><div class="wrap">
  <div class="tete" data-reveal><h2>Les gestes <em>de l'exploitation.</em></h2><p>Ici, on montre le travail plutôt que les visages. Trois gestes qui reviennent à chaque saison.</p></div>
  <div class="etapes">
    <div class="etape" data-reveal>%s<h3 style="margin-top:22px">Élever les plants</h3><p>Les jeunes cacaoyers et les jeunes palmiers grandissent en sachets, à la pépinière, avant de rejoindre la plantation.</p></div>
    <div class="etape d2" data-reveal>%s<h3 style="margin-top:22px">Sécher le cacao</h3><p>Les fèves de cacao sèchent au soleil sur des claies en bois, installées sous les palmiers.</p></div>
    <div class="etape d3" data-reveal>%s<h3 style="margin-top:22px">Conduire les ruchers</h3><p>Des ruches en bois sont posées en lisière et sous les arbres. Les abeilles y font le miel de l'exploitation.</p></div>
  </div>
</div></section>""" % (photo("reel-pepiniere-cacao.jpg","0.12","Pépinière de jeunes cacaoyers · avril 2025"), photo("reel-sechage-feves-2.jpg","0.12","Les claies de séchage, sous les palmiers"), photo("reel-ruche.jpg","0.12","Une ruche en lisière · avril 2025"))

maison += """<section class="sombre"><div class="wrap deux">
  %s
  <div data-reveal>
    <h2>Ce que nous sommes, <em>en quelques repères.</em></h2>
    <p>Pas de chiffre que nous ne pourrions pas prouver : seulement ce qui se voit sur place.</p>
    <div class="faits">
      <div><b>2006</b><span>Fondation</span></div>
      <div><b>7</b><span>Cultures</span></div>
      <div><b>2</b><span>Rivières, l'Ibenga et l'Oubangui</span></div>
      <div><b>Ibenga</b><span>District d'Enyellé, Likouala</span></div>
    </div>
  </div>
</div></section>""" % photo("reel-palmiers-2025.jpg","0.14","Palmiers à huile adultes · avril 2025")

page("l-exploitation.html", "L'exploitation", "l-exploitation.html", maison)

# ================================================================ PRODUITS
PRODUITS = [
 ("huile","Huile de palme","Huile","A-huile.jpg","Pressée sur place","Rouge, dense, parfumée. Extraite des régimes dans les jours qui suivent la récolte, avant que le fruit ne fermente. Pour la cuisine, la transformation et le détail.",[("Récolte","[ mois ]",True),("Forme","Huile brute",False),("Conditionnement","[ à fournir ]",True)],"huile-de-palme.html"),
 ("cacao","Cacao","Fèves","reel-cacao-ouvert.jpg","Récolté à maturité","Cabosses ouvertes le jour de la récolte, fèves fermentées puis séchées sur claies. Pour chocolatiers et transformateurs.",[("Récolte","[ mois ]",True),("Forme","Fèves séchées",False),("Conditionnement","[ à fournir ]",True)],"cacao.html"),
 ("safou","Safou","Fruit","A-safou.jpg","Fruit de saison","Le fruit violet de la Likouala, cueilli mûr sur l'arbre. Frais pendant la saison, transformé le reste de l'année. Un produit que peu d'exploitations proposent hors du Congo.",[("Récolte","[ mois ]",True),("Forme","Frais · transformé",False),("Conditionnement","[ à fournir ]",True)],"safou.html"),
 ("miel","Miel","Ruchers","reel-miel.jpg","Ruchers du domaine","Récolté dans les ruchers installés en lisière de forêt. Les abeilles pollinisent au passage le maïs, les légumes et les safoutiers.",[("Récolte","[ mois ]",True),("Forme","Miel · rayon",False),("Conditionnement","[ à fournir ]",True)],None),
 ("ananas","Ananas","Fruit","reel-ananas-pied.jpg","Récolté mûr","Cueilli à maturité, pas avant. Vendu frais dans le département, et sur demande au-delà.",[("Récolte","[ mois ]",True),("Forme","Frais",False),("Conditionnement","[ à fournir ]",True)],None),
 ("mais","Maïs","Vivrier","A-mais.jpg","Céréale de base","Cultivé pour le village et le marché local. En épi ou en grain, selon la demande.",[("Récolte","[ mois ]",True),("Forme","Épi · grain",False),("Conditionnement","[ à fournir ]",True)],None),
 ("legumes","Légumes","Vivrier","reel-aubergines.jpg","Frais, de saison","Aubergines africaines, gombos, piments, feuilles. La liste exacte suit la saison et reste à établir avec l'exploitation.",[("Récolte","Toute l'année · à confirmer",True),("Forme","Frais",False),("Conditionnement","[ à fournir ]",True)],None),
]
produits = hero("reel-cacao-cabosses.jpg", '<a href="index.html">Taspalm</a> · Nos produits',
    "Sept cultures,<br><em>une seule terre.</em>",
    "Trois produits emblématiques et quatre cultures de saison. Chaque fiche dit ce que nous savons, et laisse visible ce qui reste à préciser.", court=True)
idx = "".join('<a href="#%s">%s<span>%s</span></a>' % (i, n, f) for i, n, f, *_ in PRODUITS)
rang = ""
for i, n, f, img, sur, desc, mini, lien in PRODUITS:
    m = "".join('<div><span>%s</span><b%s>%s</b></div>' % (k, ' class="attente"' if a else "", v) for k, v, a in mini)
    l = ('<a class="lien" href="%s">La fiche complète</a>' % lien) if lien else '<span class="attente" style="font-size:12px">Fiche détaillée à venir</span>'
    rang += """<div class="rangee" id="%s">%s<div data-reveal><span class="sur">%s</span><h2>%s</h2><p>%s</p><div class="mini">%s</div>%s</div></div>""" % (i, photo(img,"0.12"), sur, n, desc, m, l)
produits += """<section><div class="wrap produits"><div class="index" data-reveal>%s</div><div class="defile">%s</div></div></section>""" % (idx, rang)
produits += """<section class="sombre"><div class="wrap deux" style="align-items:start"><div data-reveal><span class="sur">Professionnels</span><h2>Dites-nous <em>ce qu'il vous faut.</em></h2><p>Un produit, un usage, un volume, une destination. L'exploitation répond avec une proposition, et un échantillon si c'est utile.</p></div><div class="d2" data-reveal>%s</div></div></section>""" % echantillon_form()
page("produits.html", "Nos produits", "produits.html", produits)

# ================================================================ FICHES
H1_FICHE = {"huile-de-palme.html":"Huile de palme rouge,", "cacao.html":"Cacao,", "safou.html":"Safou,"}

def fiche(fichier, nom, em, img_hero, intro, fiche_rows, etapes, recevez, pour, gal, autres):
    c = hero(img_hero, '<a href="index.html">Taspalm</a> · <a href="produits.html">Nos produits</a> · %s' % nom,
             "%s <em>%s</em>" % (H1_FICHE.get(fichier, nom), em), intro, court=True, voile=" bas",
             actions='<a class="btn or" href="#besoin">Exprimez votre besoin</a><a class="btn ghost" href="produits.html">Toute la collection</a>')
    rows = "".join('<div><span>%s</span><b%s>%s</b></div>' % (k, ' class="attente"' if a else "", v) for k, v, a in fiche_rows)
    c += """<section class="serre"><div class="wrap"><div class="tete" data-reveal><h2>La fiche.</h2><p>Ce que nous savons est écrit ici. Ce que nous n'avons pas encore mesuré reste entre crochets, demandez-le nous.</p></div><div class="fiche" data-reveal>%s</div></div></section>""" % rows
    et = "".join('<div class="etape%s" data-reveal>%s<div class="n">%s</div><h3>%s</h3><p>%s</p></div>' % (" d%d" % (k+1) if k else "", photo(im,"0.12"), ["I","II","III"][k], t, d) for k, (im, t, d) in enumerate(etapes))
    c += """<section class="sombre"><div class="wrap"><div class="tete" data-reveal><h2>De l\'arbre <em>à vous.</em></h2><p>%s</p></div><div class="etapes">%s</div></div></section>""" % ("Trois moments.", et)
    rec = "".join('<li><b>%s</b><span>%s</span></li>' % (a, b) for a, b in recevez)
    tags = "".join('<span class="tag" style="margin:0 8px 8px 0;font-size:11px;padding:9px 12px">%s</span>' % t for t in pour)
    c += """<section><div class="wrap deux" style="align-items:start">
      <div data-reveal><span class="sur">Ce que vous recevez</span><h2>Formes et <em>conditionnements.</em></h2><ul class="liste">%s</ul><p style="margin-top:30px"><b>Pour qui</b></p><p style="margin-top:12px">%s</p></div>
      <div class="d2" data-reveal>%s</div></div></section>""" % (rec, tags, besoin_form("Votre besoin en %s" % nom.lower(), "Usage, volume, destination : l'exploitation vous répond depuis Ibenga ou Paris, avec un échantillon si c'est utile."))
    g = "".join('<div class="etape%s" data-reveal>%s</div>' % (" d2" if k else "", photo(im,"0.1",leg,h="480px")) for k, (im, leg) in enumerate(gal))
    c += '<section class="serre" style="padding-top:0"><div class="wrap"><div class="etapes" style="grid-template-columns:1fr 1fr">%s</div></div></section>' % g
    au = "".join('<a class="card%s" href="%s" data-reveal style="min-height:380px"><img src="images/%s" alt="%s" width="1024" height="1024" loading="lazy" decoding="async"><div class="cap"><span class="sur">%s</span><h3>%s</h3></div></a>' % (" d2" if k else "", h, im, alt(im), s, n2) for k, (h, im, s, n2) in enumerate(autres))
    c += """<section class="sombre"><div class="wrap"><div class="tete" data-reveal><h2>Les autres produits <em>de l'exploitation.</em></h2><p><a class="lien clair" href="produits.html">Toute la collection</a></p></div><div class="grille3" style="grid-template-columns:1fr 1fr">%s</div></div></section>""" % au
    page(fichier, nom, "produits.html", c)

fiche("huile-de-palme.html","Huile de palme","pressée sur place.","A-huile.jpg",
  "Extraite des régimes de noix de palme du domaine, dans les jours qui suivent la récolte. Dense, parfumée, pour la cuisine et la transformation.",
  [("Origine","Ibenga · Likouala",False),("Récolte","[ mois ] à confirmer",True),("Transformation","Pressage sur place",False),("Procédé","[ à préciser ] artisanal ou mécanique",True),("Forme","Huile brute non raffinée",False),("Conservation","[ à fournir ]",True),("Conditionnements","[ à fournir ] bidon, fût, détail",True),("Capacité mensuelle","[ à fournir ]",True)],
  [("reel-regime.jpg","Le régime","Les régimes sont coupés à maturité, quand les noix rougissent. Ils ne restent pas au sol."),("A-pressoir.jpg","Le pressage","Cuisson des noix, pressage, décantation. L'atelier est sur le domaine, à côté des palmiers."),("reel-barge.jpg","Le départ","Mise en bidons ou en fûts, chargement en pirogue ou en camion. Délais et destinations annoncés à la commande.")],
  [("Bidon","[ contenance à fournir ]"),("Fût","[ contenance à fournir ]"),("Détail","[ format à fournir ]"),("Échantillon","Sur demande, gratuit · à confirmer")],
  ["Distributeurs","Transformateurs","Restauration","Épiceries fines","Diaspora"],
  [("reel-noix-palme.jpg","Noix de palme détachées du régime · avril 2025"),("reel-pepiniere-palmiers.jpg","Jeunes palmiers en pépinière · avril 2025")],
  [("cacao.html","reel-cacao-ouvert.jpg","Récolté à maturité","Cacao"),("safou.html","A-safou.jpg","Fruit de saison","Safou")])

fiche("cacao.html","Cacao","fermenté puis séché au soleil.","reel-cacao-cabosses.jpg",
  "Cabosses ouvertes le jour de la récolte, fèves fermentées puis séchées sur claies au soleil. Pour chocolatiers et transformateurs qui veulent une origine unique.",
  [("Origine","Ibenga · Likouala",False),("Récolte","[ mois ] à confirmer",True),("Variété","[ à fournir ]",True),("Fermentation","Sur le domaine",False),("Durée de fermentation","[ jours ] à fournir",True),("Séchage","Sur claies, au soleil",False),("Humidité finale","[ % ] à fournir",True),("Conditionnements","[ à fournir ] sacs",True)],
  [("reel-cacao-arbre.jpg","La cabosse","Les cabosses poussent sur le tronc. Cueillies mûres, elles sont ouvertes le jour même."),("reel-cacao-ouvert.jpg","La fermentation","Sorties de la cabosse, les fèves fermentent quelques jours. C'est là que naît l'arôme."),("reel-sechage-feves.jpg","Le séchage","Sur claies, retourné plusieurs fois par jour, jusqu'à l'humidité voulue. Puis ensaché.")],
  [("Sac","[ poids à fournir ]"),("Lot minimum","[ à fournir ]"),("Échantillon","[ poids ] sur demande"),("Fiche d'analyse","À produire par l'exploitation")],
  ["Chocolatiers","Transformateurs","Torréfacteurs","Négociants d'origine"],
  [("reel-sechage-feves-2.jpg","Les claies de séchage, sous les palmiers"),("reel-cacaoyers.jpg","Cacaoyers à l'ombre des palmiers · avril 2025")],
  [("huile-de-palme.html","reel-regime.jpg","Pressée sur place","Huile de palme"),("safou.html","A-safou.jpg","Fruit de saison","Safou")])

fiche("safou.html","Safou","le fruit violet de la Likouala.","A-safoutier.jpg",
  "Cueilli mûr sur l'arbre, vendu frais pendant la saison et transformé le reste de l'année. Un fruit que peu d'exploitations proposent hors du Congo.",
  [("Origine","Ibenga · Likouala",False),("Saison","[ mois ] à confirmer",True),("Forme","Frais · transformé",False),("Transformation","[ à préciser ] séché, pâte, huile",True),("Conservation du frais","[ jours ] à fournir",True),("Conditionnements","[ à fournir ]",True),("Volume par saison","[ à fournir ]",True),("Expédition du frais","[ à confirmer ] selon destination",True)],
  [("A-safoutier.jpg","L'arbre","Le safoutier donne une fois l'an. Les fruits passent du rose au violet foncé quand ils sont prêts."),("A-safou.jpg","La cueillette","Cueilli à la main, à maturité. Le safou ne se conserve pas longtemps frais, tout se joue en quelques jours."),("A-pirogue.jpg","Le voyage","Frais vers les villes proches, transformé pour aller plus loin.")],
  [("Frais","[ conditionnement à fournir ]"),("Transformé","[ forme à fournir ]"),("Échantillon","Frais en saison · transformé hors saison"),("Disponibilité","[ mois ] à confirmer")],
  ["Épiceries africaines","Restauration","Diaspora","Transformateurs"],
  [("A-safou.jpg","Safous sur feuille · image d'illustration"),("reel-confluence.jpg","Confluence de deux rivières · septembre 2021")],
  [("huile-de-palme.html","reel-regime.jpg","Pressée sur place","Huile de palme"),("cacao.html","reel-cacao-ouvert.jpg","Récolté à maturité","Cacao")])

# ================================================================ TERROIR
CARTE = """<svg viewBox="0 0 600 420" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Schéma de situation">
<defs><linearGradient id="riv" x1="0" x2="1"><stop offset="0" stop-color="#8A6A4A"/><stop offset="1" stop-color="#B08A5E"/></linearGradient></defs>
<rect width="600" height="420" fill="#16402F"/>
<path d="M40 60 C120 40 180 120 240 150 S330 190 360 250 S420 340 470 400" fill="none" stroke="url(#riv)" stroke-width="26" stroke-linecap="round" opacity=".9"/>
<path d="M470 0 C440 80 420 150 400 200 S370 270 360 250" fill="none" stroke="url(#riv)" stroke-width="16" stroke-linecap="round" opacity=".8"/>
<text x="60" y="45" fill="#F4EFE4" font-family="Cormorant Garamond,serif" font-size="22" font-style="italic">Oubangui</text>
<text x="482" y="120" fill="#F4EFE4" font-family="Cormorant Garamond,serif" font-size="22" font-style="italic">Ibenga</text>
<circle cx="330" cy="215" r="34" fill="#C89A3A" opacity=".18"/><circle cx="330" cy="215" r="7" fill="#C89A3A"/>
<text x="352" y="210" fill="#F4EFE4" font-family="Manrope,sans-serif" font-size="12" letter-spacing="2">DOMAINE · IBENGA</text>
<text x="352" y="228" fill="rgba(244,239,228,.6)" font-family="Manrope,sans-serif" font-size="11">position schématique</text>
<text x="500" y="395" fill="rgba(244,239,228,.5)" font-family="Manrope,sans-serif" font-size="11" letter-spacing="2">RDC →</text>
<text x="40" y="395" fill="rgba(244,239,228,.5)" font-family="Manrope,sans-serif" font-size="11" letter-spacing="2">← IMPFONDO</text>
</svg>"""
terroir = hero("hero-domaine-1600.jpg", '<a href="index.html">Taspalm</a> · Le terroir',
    "Une terre entre <em>deux rivières.</em>",
    "Ibenga, district d'Enyellé, département de la Likouala, au nord de la République du Congo. Là où l'Ibenga rejoint l'Oubangui.", court=True, voile=" bas")
terroir += """<section><div class="wrap deux">
  <div data-reveal>
    <span class="sur">Où nous sommes</span>
    <h2>Ibenga, <em>Enyellé,</em> Likouala.</h2>
    <p>Le domaine est bordé par la rivière Ibenga, près de sa confluence avec l'Oubangui, qui marque la frontière avec la République démocratique du Congo.</p>
    <p>On y arrive par la rivière ou par la route depuis Impfondo, chef-lieu du département.</p>
    <div class="faits clair">
      <div><b>2006</b><span>Installation</span></div>
      <div><b>Ibenga</b><span>Village</span></div>
      <div><b>Enyellé</b><span>District</span></div>
      <div><b>Likouala</b><span>Département</span></div>
    </div>
  </div>
  <div class="carte-svg d2" data-reveal>%s<div class="leg">Schéma de situation, sans échelle</div></div>
</div></section>""" % CARTE
terroir += """<section class="sombre"><div class="wrap">
  <div class="tete" data-reveal><h2>Ce que la terre <em>donne.</em></h2><p>Trois éléments qui font le domaine, tels qu'on les voit sur place.</p></div>
  <div class="etapes">
    <div class="etape" data-reveal>%s<div class="n">Le sol</div><h3>Une terre travaillée en buttes</h3><p>Les ananas et les cultures vivrières sont plantés sur des buttes de terre meuble.</p></div>
    <div class="etape d2" data-reveal>%s<div class="n">L'ombre</div><h3>Des cultures qui se protègent</h3><p>Les cacaoyers grandissent à l'ombre des palmiers et des grands arbres, les ruches sont posées en lisière.</p></div>
    <div class="etape d3" data-reveal>%s<div class="n">L'eau</div><h3>La rivière, chemin et frontière</h3><p>Elle borde le domaine, elle transporte les récoltes, elle marque la frontière.</p></div>
  </div>
</div></section>""" % (photo("reel-sol.jpg","0.12","Ananas plantés sur buttes · avril 2025"), photo("reel-cacaoyers.jpg","0.12","Cacaoyers à l'ombre des palmiers · avril 2025"), photo("reel-riviere-portrait.jpg","0.12","La rivière · janvier 2018"))
terroir += """<section><div class="wrap deux">
  %s
  <div data-reveal>
    <h2>Notre façon de faire, <em>telle qu'on la voit sur place.</em></h2>
    <p>Des gestes simples, répétés à chaque saison.</p>
    <ul class="liste">
      <li><b>Élever nos plants</b><span>À la pépinière du domaine</span></li>
      <li><b>Associer les cultures</b><span>Le cacao à l'ombre des palmiers</span></li>
      <li><b>Garder des abeilles</b><span>Des ruches en lisière</span></li>
      <li><b>Sécher au soleil</b><span>Sur claies, sous les palmiers</span></li>
    </ul>
  </div>
</div></section>""" % photo("reel-pepiniere-sacs.jpg","0.14","Jeunes plants à la pépinière · avril 2022")
terroir += """<section class="encre"><div class="wrap deux">
  %s
  <div data-reveal>
    <h2 class="citation">Une exploitation qui tourne, c'est des emplois qui ne demandent pas de partir à Brazzaville, <em>et des savoir-faire qui restent à Ibenga.</em></h2>
    <p style="margin-top:30px"><a class="btn or" href="visiter.html">Venir voir</a></p>
  </div>
</div></section>""" % photo("reel-village.jpg","0.14","Village de la Likouala · janvier 2018", h="560px")
page("terroir.html", "Le terroir", "terroir.html", terroir)

# ================================================================ PROFESSIONNELS
pro = hero("reel-barge.jpg", '<a href="index.html">Taspalm</a> · Professionnels',
    "Acheter, transformer, <em>distribuer.</em>",
    "L'exploitation fournit en direct, sans intermédiaire. Quatre façons de travailler ensemble, un seul point de départ : votre besoin.", court=True, voile=" bas",
    actions="""<a class="btn or" href="#besoin">Exprimez votre besoin</a><a class="btn ghost" href="__WA__" target="_blank" rel="noopener">Discuter sur WhatsApp</a>""")
pro += """<section class="sombre"><div class="wrap">
  <div class="tete" data-reveal><h2>Quatre façons de travailler <em>avec l'exploitation.</em></h2><p>Chaque voie a son interlocuteur. Aucune ne passe par un formulaire générique.</p></div>
  <div class="publics">
    <div class="public" data-reveal><span class="sur">Acheter</span><h3>Distributeurs et revendeurs</h3><p>Huile, cacao, safou, miel, en gros ou au détail, avec des volumes engagés sur la saison.</p><a class="lien clair" href="#besoin">Exprimez votre besoin</a></div>
    <div class="public d2" data-reveal><span class="sur">Transformer</span><h3>Industriels agroalimentaires</h3><p>Matière première brute ou semi-transformée, à cahier des charges.</p><a class="lien clair" href="#besoin">Exprimez votre besoin</a></div>
    <div class="public d3" data-reveal><span class="sur">Servir</span><h3>Restauration et hôtellerie</h3><p>Approvisionnement en huile, fruits et légumes, selon les saisons.</p><a class="lien clair" href="#besoin">Exprimez votre besoin</a></div>
    <div class="public d4" data-reveal><span class="sur">Financer</span><h3>Partenaires et investisseurs</h3><p>Extension des surfaces, équipement de transformation, logistique fluviale. Parlons-en.</p><a class="lien clair" href="#besoin">Exprimez votre besoin</a></div>
  </div>
</div></section>"""
pro += """<section><div class="wrap">
  <div class="tete" data-reveal><h2>Comment ça se passe, <em>en quatre temps.</em></h2><p>Du premier message à la livraison, quatre étapes simples.</p></div>
  <div class="chrono" data-reveal><ol style="grid-template-columns:repeat(4,1fr)">
    <li><b>I</b><p><strong>Le besoin.</strong> Vous nous dites le produit, l'usage, le volume et la destination. Nous répondons, avec un échantillon si c'est utile.</p></li>
    <li><b>II</b><p><strong>Le devis.</strong> Volume, conditionnement, conditions de livraison. Une page, pas dix.</p></li>
    <li><b>III</b><p><strong>La commande.</strong> Une fois le devis accepté, la récolte ou le lot vous est réservé.</p></li>
    <li><b>IV</b><p><strong>La livraison.</strong> Par la rivière puis par la route, vers la destination convenue ensemble.</p></li>
  </ol></div>
</div></section>"""
pro += """<section class="encre"><div class="wrap deux">
  <div data-reveal><h2>Une question avant de commander ? <em>Écrivez-nous sur WhatsApp.</em></h2><p>Volumes, conditionnement, livraison : l'exploitation vous répond directement, depuis Ibenga ou depuis Paris.</p><p style="margin-top:30px"><a class="btn wa" href="__WA__" target="_blank" rel="noopener">__ICO__Discuter sur WhatsApp</a></p></div>
  %s
</div></section>""" % photo("reel-ananas-champ.jpg","0.14","Champ d'ananas au lever du jour · avril 2025", h="520px")
pro += """<section><div class="wrap deux" style="align-items:start">
  <div data-reveal><h2>Dites-nous <em>ce qu'il vous faut.</em></h2><p>Un produit, un usage, un volume, une destination. L'exploitation répond avec une proposition, et un échantillon si c'est utile.</p></div>
  <div class="d2" data-reveal>%s</div>
</div></section>""" % echantillon_form()
page("professionnels.html", "Professionnels", "professionnels.html", pro)

# ================================================================ VISITER
vis = hero("reel-riviere.jpg", '<a href="index.html">Taspalm</a> · Visiter',
    "Venir à Ibenga, <em>voir de ses yeux.</em>",
    "L'exploitation reçoit des visiteurs, des étudiants et des porteurs de projet. On marche dans la plantation, on assiste au pressage, on goûte.", court=True, voile=" bas",
    actions='<a class="btn or" href="#visite">Préparer une visite</a>')
vis += """<section><div class="wrap">
  <div class="tete" data-reveal><h2>Une journée <em>sur l'exploitation.</em></h2><p>Un exemple de journée, à ajuster selon la saison et ce que vous venez chercher.</p></div>
  <div class="etapes">
    <div class="etape" data-reveal>%s<div class="n">Le matin</div><h3>La plantation</h3><p>Palmiers, cacaoyers, safoutiers, ruchers en lisière. On marche, on cueille, on explique ce qui pousse et quand.</p></div>
    <div class="etape d2" data-reveal>%s<div class="n">Midi</div><h3>L'atelier</h3><p>Le séchage du cacao, le pressage de l'huile, selon la saison. On regarde, on sent, on comprend pourquoi ça se fait ici.</p></div>
    <div class="etape d3" data-reveal>%s<div class="n">Le soir</div><h3>La rivière</h3><p>Le chargement des pirogues, le village. On goûte ce qu'on a vu pousser.</p></div>
  </div>
</div></section>""" % (photo("reel-piste.jpg","0.12","La piste du domaine · avril 2025"), photo("reel-sechage-feves.jpg","0.12","Le séchage du cacao"), photo("reel-riviere-portrait.jpg","0.12","La rivière · janvier 2018"))
vis += """<section class="sombre"><div class="wrap deux">
  %s
  <div data-reveal><span class="sur">Pratique</span><h2>Y aller, <em>y rester.</em></h2>
    <ul class="liste">
      <li><b>Depuis Brazzaville</b><span>[ vol vers Impfondo, à confirmer ]</span></li>
      <li><b>Depuis Impfondo</b><span>[ route ou rivière · durée à fournir ]</span></li>
      <li><b>Hébergement</b><span>[ au village ou à Enyellé, à confirmer ]</span></li>
      <li><b>Saison recommandée</b><span>[ mois à confirmer ]</span></li>
      <li><b>Formalités</b><span>[ à préciser ]</span></li>
    </ul>
  </div>
</div></section>""" % photo("reel-village.jpg","0.14","Village de la Likouala · janvier 2018")
vis += """<section><div class="wrap deux" style="align-items:start">
  <div data-reveal><span class="sur">Formats</span><h2>Visite, immersion, <em>formation.</em></h2><p>Trois formules, organisées sur demande. Écrivez-nous pour construire la vôtre.</p>
    <p style="margin-top:22px"><a class="btn wa" href="__WA__" target="_blank" rel="noopener">__ICO__Discuter sur WhatsApp</a></p>
    <ul class="liste">
      <li><b>La visite</b><span>Une journée · Sur devis</span></li>
      <li><b>L'immersion</b><span>Trois jours · Sur devis</span></li>
      <li><b>La formation</b><span>Cacao ou apiculture · Sur devis</span></li>
    </ul></div>
  <form class="form d2" id="visite" data-reveal method="post" action="envoyer.php" accept-charset="UTF-8">
    <h3>Préparer une visite</h3><p>Dites-nous qui vous êtes et ce que vous venez voir. L'exploitation vous répond avec les dates possibles.</p>
    <input type="hidden" name="formulaire" value="visite"><input type="hidden" name="langue" value="fr"><input type="hidden" name="page" value=""><input type="hidden" name="t" value=""><div class="pot" aria-hidden="true"><label>Ne pas remplir<input type="text" name="site_web" tabindex="-1" autocomplete="off"></label></div>
    <label for="v-nom">Votre nom</label><input id="v-nom" name="nom" type="text" maxlength="120" autocomplete="name">
    <label for="v-qui">Vous venez en tant que</label><select id="v-qui" name="profil"><option>Visiteur</option><option>Étudiant</option><option>Porteur de projet</option><option>Acheteur</option><option>Presse</option></select>
    <label for="v-quand">Période envisagée</label><input id="v-quand" name="periode" type="text" maxlength="120">
    <label for="v-mail">Email ou WhatsApp</label><input id="v-mail" name="contact" type="text" maxlength="160" required minlength="5">
    <button class="btn vert" type="submit">Envoyer</button>
    <p class="note">Votre message est envoyé à l'exploitation et sert uniquement à vous répondre. <a href="confidentialite.html">Confidentialité</a></p>
  </form>
</div></section>"""
page("visiter.html", "Visiter", "visiter.html", vis)

# ================================================================ CONTACT
contact = hero("reel-palmiers.jpg", '<a href="index.html">Taspalm</a> · Contact',
    "Écrire <em>à l'exploitation.</em>",
    "Une seule adresse, deux pays, des gens qui répondent.", court=True, voile=" bas")
contact += """<section><div class="wrap deux" style="align-items:start">
  <p class="alerte" id="alerte-envoi" hidden>Votre message n'a pas pu partir. Vérifiez que le champ « Email ou WhatsApp » est rempli, patientez une minute, puis réessayez. Vous pouvez aussi appeler le +242 05 536 16 05.</p>
  <div data-reveal>
    <span class="sur">Coordonnées</span>
    <h2>Ibenga <em>et Paris.</em></h2>
    <ul class="liste">
      <li><b>Écrire</b><span>contact@taspalm.com<br><em style="font-weight:400;letter-spacing:0;text-transform:none;color:#9A9282">adresse unique à créer</em></span></li>
      <li><b>Congo</b><span>+242 05 536 16 05<br>+242 06 993 23 64</span></li>
      <li><b>Europe</b><span>+33 7 80 73 53 82<br>+33 6 49 10 66 50</span></li>
      <li><b>WhatsApp</b><span><a href="__WA__" target="_blank" rel="noopener">+242 06 993 23 64</a></span></li>
      <li><b>Le domaine</b><span>Ibenga, district d'Enyellé<br>Likouala, République du Congo</span></li>
    </ul>
  </div>
  <form class="form d2" data-reveal method="post" action="envoyer.php" accept-charset="UTF-8">
    <h3>Nous écrire</h3><p>Pour tout ce qui n'est ni un besoin produit ni une visite.</p>
    <input type="hidden" name="formulaire" value="contact"><input type="hidden" name="langue" value="fr"><input type="hidden" name="page" value=""><input type="hidden" name="t" value=""><div class="pot" aria-hidden="true"><label>Ne pas remplir<input type="text" name="site_web" tabindex="-1" autocomplete="off"></label></div>
    <label for="c-nom">Votre nom</label><input id="c-nom" name="nom" type="text" maxlength="120" autocomplete="name">
    <label for="c-mail">Email ou WhatsApp</label><input id="c-mail" name="contact" type="text" maxlength="160" required minlength="5">
    <label for="c-msg">Votre message</label><textarea id="c-msg" name="message" rows="5" maxlength="3000" required minlength="5"></textarea>
    <button class="btn vert" type="submit">Envoyer</button>
    <p class="note">Votre message est envoyé à l'exploitation et sert uniquement à vous répondre. <a href="confidentialite.html">Confidentialité</a></p>
  </form>
</div></section>"""
page("contact.html", "Contact", "", contact)

# ================================================================ MERCI
merci = hero("reel-palmiers.jpg", "", "C'est parti, <em>merci.</em>", "Votre message est arrivé à l'exploitation. Nous vous répondons depuis Ibenga ou depuis Paris, à l'adresse ou au numéro que vous avez laissé.", court=True, voile=" bas", actions="""<a class="btn or" href="index.html">Revenir à l'accueil</a><a class="btn ghost" href="produits.html">Voir la collection</a>""")
page("merci.html", "Message envoyé", "", merci)

# ================================================================ MENTIONS
mentions = hero("reel-palmiers.jpg", '<a href="index.html">Taspalm</a> · Mentions légales', "Mentions <em>légales.</em>", "Les informations ci-dessous sont à fournir par l'exploitation avant mise en ligne.", court=True, voile=" bas")
mentions += """<section><div class="wrap" style="max-width:820px"><div data-reveal>
  <ul class="liste">
    <li><b>Éditeur</b><span>[ raison sociale, forme juridique, capital ]</span></li>
    <li><b>Siège</b><span>[ adresse ]</span></li>
    <li><b>Immatriculation</b><span>[ RCCM, NIU ]</span></li>
    <li><b>Directeur de la publication</b><span>[ nom ]</span></li>
    <li><b>Hébergeur</b><span>[ prestataire ]</span></li>
    <li><b>Données personnelles</b><span>[ usage des formulaires, durée de conservation ]</span></li>
    <li><b>Crédits</b><span>Conception : Yann Tassoua · photographies : [ à créditer ]</span></li>
  </ul></div></div></section>"""
page("mentions-legales.html", "Mentions légales", "", mentions)


# ================================================================ CONFIDENTIALITÉ
conf = hero("reel-palmiers.jpg", '<a href="index.html">Taspalm</a> · Confidentialité', "Vos données, <em>et ce que nous en faisons.</em>", "Ce site ne dépose aucun traceur et ne mesure pas son audience. Voici ce qu'il collecte, et ce qu'il ne collecte pas.", court=True, voile=" bas")
conf += """<section><div class="wrap" style="max-width:820px"><div data-reveal>
  <ul class="liste">
    <li><b>Traceurs et mesure d'audience</b><span>Aucun. Pas de cookie, pas d'outil de statistiques.</span></li>
    <li><b>Polices de caractères</b><span>Hébergées sur ce site. Aucun appel vers un service tiers.</span></li>
    <li><b>Formulaires</b><span>Vos messages arrivent dans la boîte e-mail de l'exploitation (messagerie Gmail, Google). Ils servent uniquement à vous répondre. Conservation : [ durée à définir ]</span></li>
    <li><b>Hébergeur</b><span>[ OVHcloud, à confirmer ] · sous-traitant technique</span></li>
    <li><b>Vos droits</b><span>Accès, rectification, suppression : écrire à [ adresse à créer ]</span></li>
    <li><b>Responsable du traitement</b><span>[ raison sociale, adresse ]</span></li>
  </ul>
  <p style="margin-top:22px;font-size:14px;color:var(--encre2)">Page gabarit, à compléter avant le branchement des formulaires. Les crochets sont à remplir par l'exploitation.</p>
</div></div></section>"""
page("confidentialite.html", "Confidentialité", "", conf)

# ---------------------------------------------------------------- fichiers communs
open(os.path.join(WWW, "styles.css"), "w").write(CSS)
open(os.path.join(WWW, "site.js"), "w").write(JS)
shutil.copy(os.path.join(B, "php", "envoyer.php"), os.path.join(WWW, "envoyer.php"))
PAGES_SM=["index.html","l-exploitation.html","produits.html","huile-de-palme.html","cacao.html","safou.html","terroir.html","professionnels.html","visiter.html","contact.html"]
for _a in list(PAGES): page(*_a, lang="en")
if MANQUANTS:
    open(os.path.join(B,"_a-traduire.txt"),"w").write("\n".join(sorted(MANQUANTS)))
    print("TRADUCTIONS MANQUANTES :", len(MANQUANTS), "→ _a-traduire.txt")
else: print("traduction complète")
open(os.path.join(WWW,"sitemap.xml"),"w").write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+"".join('  <url><loc>%s/%s</loc><changefreq>%s</changefreq><priority>%s</priority></url>\n' % (SITE_URL, "" if p=="index.html" else p, "weekly" if p=="index.html" else "monthly", "1.0" if p=="index.html" else "0.8" if p in ("produits.html","huile-de-palme.html","cacao.html","safou.html") else "0.6") for p in PAGES_SM)+"".join('  <url><loc>%s/en/%s</loc><changefreq>monthly</changefreq><priority>%s</priority></url>\n' % (SITE_URL, "" if p=="index.html" else p, "0.9" if p=="index.html" else "0.7") for p in PAGES_SM)+'</urlset>\n')
open(os.path.join(WWW,"robots.txt"),"w").write("User-agent: *\nAllow: /\nDisallow: /mentions-legales.html\nDisallow: /confidentialite.html\nSitemap: %s/sitemap.xml\n" % SITE_URL)
open(os.path.join(WWW, "favicon.svg"), "w").write('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><circle cx="32" cy="32" r="30" fill="#0E2E24"/><circle cx="32" cy="32" r="24" fill="none" stroke="#C89A3A" stroke-width="2"/><text x="32" y="42" text-anchor="middle" font-family="Cormorant Garamond,Georgia,serif" font-size="30" fill="#C89A3A">T</text></svg>')
print("terminé ·", WWW)
