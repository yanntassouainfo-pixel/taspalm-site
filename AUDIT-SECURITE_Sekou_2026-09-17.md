# Rapport d'audit pré-production : site Taspalm, direction A « L'Exploitation »

**Verdict : GO sous conditions.** Le site peut être mis en ligne une fois le fichier `.htaccess` déposé et vérifié (en-têtes lus sur le site réel), le dossier `www/` seul transféré par SFTP, et la page Mentions légales complétée par le client. Aucun point critique dans le code livré.

Auditeur : Sekou, sécurité Oya. Date : 17 septembre 2026. Fonction NIST couverte : Identify et Protect, avec un plan Respond / Recover minimal en fin de rapport.

---

## 1. Périmètre et méthode

**Périmètre audité**

- `PROJETS/taspalm/refonte-2026-09-17/site-A/www/` : 11 pages HTML (`index`, `l-exploitation`, `produits`, `huile-de-palme`, `cacao`, `safou`, `terroir`, `professionnels`, `visiter`, `contact`, `mentions-legales`), `styles.css`, `site.js`, `favicon.svg`, 20 images JPG (4,0 Mo).
- Le générateur `site-A/build.py` et `render.py`, lus pour vérifier qu'ils ne contiennent ni secret ni chemin à ne pas publier.
- Cible d'hébergement annoncée : OVH mutualisé, offre Perso, Apache, certificat Let's Encrypt, dépôt par FTP, pas de base de données.

**Autorisation** : projet Oya en cours pour le client Taspalm, ce qui vaut autorisation pour ce livrable. Aucun test actif n'a été mené : lecture des fichiers uniquement, plus recherche documentaire sur les fonctions OVH.

**Ce qui n'est pas dans le périmètre** : l'hébergement lui-même (pas encore ouvert), le nom de domaine, les boîtes e-mail, le compte OVH du client. Ces points apparaissent dans le rapport comme « dépend du client ».

**Méthode** : grille OWASP en lecture défensive, adaptée à un site statique (pas d'authentification, pas de base de données, pas de traitement côté serveur). Balayage automatisé de toutes les pages pour les ressources externes, attributs `rel` et `target`, gestionnaires d'événements inline, scripts inline, styles inline, formulaires, liens internes, métadonnées d'images, motifs de secrets.

---

## 2. Constats

### Critique

Aucun.

### Important (à traiter avant la mise en ligne)

**I-1. Aucun en-tête de sécurité HTTP, listage de répertoires non bloqué, HTTPS non forcé.**
Statut : à corriger. Assigné à Moussa. Délai proposé à Kofi : avant le premier dépôt FTP.
Impact en clair : sans redirection, un visiteur qui tape `http://` voit le site en clair et un réseau hostile (wifi public) peut modifier la page en transit. Sans `Options -Indexes`, l'adresse `/images/` peut afficher la liste de tous les fichiers du dossier. Sans en-têtes, le site peut être affiché dans un cadre sur un site tiers (détournement de clic) et un script injecté par une future erreur d'intégration s'exécuterait sans frein.
Remédiation : déposer le fichier `htaccess-recommande.txt` renommé en `.htaccess` à la racine du site. Il couvre HTTPS forcé, HSTS (24 h la première semaine, puis un an), `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, une CSP compatible Google Fonts, le blocage des fichiers de travail et des fichiers cachés. Après dépôt, Moussa vérifie les en-têtes servis avec `curl -I` et me renvoie la sortie : « corrigé » signifie re-vérifié.

**I-2. Google Fonts chargé depuis les serveurs de Google sur les 11 pages.**
Statut : à décider, puis à corriger si le client vise des visiteurs européens (c'est le cas : Paris est annoncé comme point de contact). Assigné à Moussa, décision Kofi et client.
Impact en clair : à chaque visite, le navigateur appelle `fonts.googleapis.com` puis `fonts.gstatic.com`, et transmet donc l'adresse IP du visiteur à Google avant tout consentement. Un tribunal allemand (Munich, janvier 2022) a jugé ce chargement contraire au RGPD ; la lecture dominante des CNIL européennes va dans le même sens. Deuxième effet : si Google Fonts est lent ou inaccessible (réseaux congolais, coupures), le texte s'affiche avec les polices de secours. Niveau de preuve sur la décision de Munich : croisé (relayé par plusieurs sources spécialisées, jugement non rouvert dans cet audit).
Remédiation : rapatrier les deux familles (Cormorant Garamond et Manrope, distribuées sous licence libre SIL OFL selon Google Fonts ; à confirmer sur la page de chaque police au moment du téléchargement) en fichiers `.woff2` dans `www/fonts/`, les déclarer par `@font-face` dans `styles.css`, retirer les deux balises `<link>` Google dans `build.py`. Une heure de travail environ. La CSP passe alors à sa variante « sans Google » (déjà écrite en commentaire dans le `.htaccess`). Si le client refuse, l'information doit figurer dans la page Confidentialité (voir I-4).

**I-3. Formulaires non branchés : ce qu'il faudra exiger le jour du branchement.**
Statut : conforme aujourd'hui (les boutons pointent sur `href="#"`, aucune donnée ne part nulle part, aucun élément `<form>` n'existe). Assigné à Moussa pour la suite, Sekou re-vérifie avant activation.
Ce qui existe : quatre formulaires visuels (échantillon sur 7 pages, contact, visite), champs `type="text"` partout y compris pour l'e-mail, aucune validation, aucun anti-spam, aucune mention d'information, pas d'attribut `name` ni `required`.
Exigences au branchement, sans lesquelles je rendrai un NO-GO sur cette partie :
1. Un vrai `<form method="post">` avec attributs `name`, `required`, `maxlength`, `type="email"` quand c'est un e-mail, `autocomplete` correct.
2. Validation côté serveur de chaque champ (longueur, format), quel que soit le mécanisme choisi (script PHP sur l'hébergement OVH, ou service tiers).
3. Anti-spam sans CAPTCHA visuel dans un premier temps : champ pot de miel caché, contrôle du délai de soumission, limitation de fréquence côté serveur. Un CAPTCHA tiers (Google, Cloudflare) ajoute un appel externe et une question RGPD ; à n'ajouter que si le spam le justifie.
4. Si l'envoi passe par un script d'e-mail : nettoyage des retours à la ligne dans les champs réinjectés dans les en-têtes du message (sinon le formulaire devient un relais de spam), destinataire codé en dur, jamais lu depuis le formulaire.
5. Si l'envoi passe par un service tiers (Formspree, Web3Forms, Brevo ou équivalent) : ajouter son domaine dans `form-action` et `connect-src` de la CSP, l'inscrire comme sous-traitant dans la page Confidentialité, choisir un hébergement des données en Union européenne.
6. Mention d'information sous chaque bouton d'envoi : qui reçoit, pour quoi, combien de temps c'est conservé, comment demander la suppression, avec lien vers la page Confidentialité. Pas de case à cocher obligatoire pour une simple demande de contact ; en revanche, une case explicite si un jour on ajoute une lettre d'information.
7. Un test de bout en bout avec moi avant activation : envoi réel, réception, données visibles nulle part dans l'URL.

**I-4. Mentions légales vides et page Confidentialité inexistante.**
Statut : dépend du client pour le contenu, Moussa pour l'intégration. Assigné : client (Amani collecte), Moussa intègre.
Impact en clair : la page `mentions-legales.html` affiche des crochets à remplir (éditeur, siège, immatriculation RCCM et NIU, directeur de publication, hébergeur, données personnelles). Le pied de page affiche « Confidentialité » en texte simple, sans lien, et aucune page n'existe. Un site professionnel mis en ligne avec ces trous expose l'exploitation à une remarque légale plutôt qu'à une attaque, mais c'est un préalable à la mise en ligne, et la page Confidentialité devient obligatoire le jour où les formulaires ou les polices Google collectent quelque chose.
Remédiation : Amani récupère les sept informations auprès du client ; Moussa crée `confidentialite.html` (données collectées, finalité, durée, hébergeur OVH comme sous-traitant, Google si les polices restent chez Google, droits d'accès et de suppression, adresse de contact) et transforme le mot « Confidentialité » en lien. Le droit congolais des données personnelles n'a pas été vérifié dans cet audit ; le RGPD s'applique dès lors que le site s'adresse à des visiteurs en Europe.

**I-5. Transfert des fichiers : FTP en clair et périmètre du dépôt.**
Statut : dépend du client (compte OVH), consigne pour Moussa.
Impact en clair : le FTP classique envoie le mot de passe en clair sur le réseau. Une seule connexion depuis un wifi non maîtrisé suffit à le faire lire. Deuxième risque, plus fréquent : déposer par erreur `build.py`, `build.py.bak-maison-2026-09-17`, le PDF de 6 Mo, les dossiers `rendus/` et `_artifact-site/`, ou les fichiers cachés `.DS_Store` que macOS crée dans chaque dossier. Le `.htaccess` bloque leur lecture par le web, mais mieux vaut ne pas les envoyer.
Remédiation : activer SFTP sur l'utilisateur FTP dans l'espace client OVH, onglet « FTP - SSH », colonne SFTP (fonction documentée par OVH pour l'offre Perso, port 22 ; niveau de preuve : vérifié sur la documentation OVH). Configurer FileZilla en SFTP. Ne transférer que le contenu de `www/` plus le `.htaccess`. Ajouter un filtre FileZilla qui exclut `.DS_Store`. Mot de passe FTP généré par un gestionnaire de mots de passe, 20 caractères minimum, jamais transmis par WhatsApp ou e-mail en clair, jamais communiqué à Sekou.

### Recommandé (à traiter dans le mois)

**R-1. Compte OVH du client : double authentification et moindre privilège.**
Dépend du client. Activer la 2FA sur le compte OVH (application d'authentification ou clé physique ; fonction documentée par OVH, niveau vérifié). Si Oya doit accéder à l'hébergement, préférer un utilisateur FTP dédié à Oya, révocable, plutôt que le mot de passe principal. L'adresse e-mail de récupération du compte OVH doit elle-même être protégée par 2FA : c'est presque toujours par l'e-mail qu'un compte d'hébergement se fait reprendre.

**R-2. Sauvegardes : la source de vérité est locale, pas chez l'hébergeur.**
Assigné à Moussa et Amani. Le site est entièrement régénérable depuis `build.py` et le dossier `images/` source, versionnés dans le dépôt git de l'agence. C'est la meilleure sauvegarde possible pour un site statique, à condition que le dépôt soit lui-même poussé hors du poste de Yann (dépôt distant à jour, et la règle 3-2-1 : trois copies, deux supports, une hors site). OVH propose une restauration de l'espace de stockage depuis l'espace client (documentée ; l'étendue exacte sur l'offre Perso n'a pas été vérifiée dans cet audit). À faire une fois : après la mise en ligne, archiver une copie datée de `www/` telle que déployée, et tester une restauration complète par simple re-dépôt SFTP. Une sauvegarde jamais restaurée n'est pas une sauvegarde.

**R-3. Numéros de téléphone personnels publiés.**
Dépend du client. Quatre numéros de mobile (deux Congo, deux Europe) figurent dans le pied de page de chaque page et sur la page Contact. Ils sont repris du site actuel (marqué « vérifié · site actuel » dans la maquette). Un numéro de mobile est une donnée personnelle de la personne qui le porte : le client doit confirmer que chaque titulaire accepte cette publication, et nommer qui répond à quel numéro. Point d'attention, pas d'alerte.

**R-4. Adresse e-mail annoncée avant d'exister.**
Dépend du client. La page Contact affiche `contact@taspalm.com` avec la mention « adresse unique à créer ». Créer la boîte avant la mise en ligne (et la protéger par un mot de passe fort, car c'est elle qui recevra plus tard les formulaires). Pas de lien `mailto:` dans le code : bon choix contre la collecte automatique par les robots à spam.

**R-5. Texte de chantier visible.**
Hors sécurité, signalé à Kofi. Les mentions « coordonnées à fournir », « [ ha ] », « image d'illustration · à remplacer », « document à produire » et « Le formulaire sera activé prochainement » sont volontaires à ce stade de maquette. Elles doivent être arbitrées avant la mise en ligne publique : un visiteur professionnel les lira.

**R-6. Bouton « Télécharger le dossier » sur `href="#"`.**
Assigné à Moussa. Le jour où le PDF existe, le déposer dans `www/` sous un nom sans espace ni accent, et vérifier qu'il ne contient pas de métadonnées inutiles (auteur, logiciel, chemin local) avant publication.

---

## 3. Points vérifiés conformes

Pour que Kofi sache ce qui est couvert.

| Point | Constat | Niveau |
|---|---|---|
| Secrets en clair | Aucun mot de passe, clé, jeton, identifiant FTP, adresse SMTP dans `www/`, `build.py`, `render.py` | Vérifié |
| Scripts inline et gestionnaires `onclick` | Aucun. Un seul script, `site.js`, externe, sur les 11 pages | Vérifié |
| Contenu de `site.js` | Animation au défilement, menu mobile, index produits. Aucun `innerHTML`, aucun `eval`, aucune requête réseau, aucune lecture de paramètre d'URL. Les sélecteurs sont construits sur des `href` statiques issus du générateur | Vérifié |
| Ressources externes | Deux domaines Google Fonts seulement. Aucun CDN, aucun outil de mesure d'audience, aucune iframe, aucun `<object>` ou `<embed>` | Vérifié |
| Liens externes et `rel` | Aucun lien sortant, aucun `target="_blank"`, donc pas d'exposition `noopener` à ce jour. Règle pour la suite : tout lien `target="_blank"` porte `rel="noopener noreferrer"` | Vérifié |
| Liens internes | Les 11 pages, toutes les ancres (`#echantillon`, `#dossier`, `#miel`...), toutes les images référencées existent. Seuls liens morts : les 9 boutons d'envoi sur `href="#"`, volontaires | Vérifié |
| Métadonnées des images | 0 image sur 20 avec EXIF, GPS ou auteur : la conversion PNG vers JPG par `build.py` les a retirées | Vérifié |
| Fichiers indésirables dans `www/` | Aucun `.DS_Store`, `.bak`, `.md`, `.py` au moment de l'audit | Vérifié (à re-vérifier après chaque `build.py`) |
| Exposition d'informations dans le HTML | Aucun commentaire HTML, aucune balise `generator`, aucun chemin local. Le commentaire d'entête de `site.js` crédite « Yann Tassoua 2026-09 », en cohérence avec la page Mentions légales | Vérifié |
| `mailto:` | Absent, l'e-mail est affiché en texte : freine la collecte par robots | Vérifié |
| Certificat HTTPS | Let's Encrypt inclus par défaut sur les offres Kimsufi Web, Perso, Pro, Performance selon la documentation OVH ; généré après rattachement du domaine au multisite avec l'option SSL cochée | Vérifié (documentation OVH), à constater sur le site réel |
| Formulaires | Inertes, aucune donnée collectée aujourd'hui | Vérifié |

---

## 4. Plan minimal de réponse à incident (site statique, sans base de données)

Un site statique a un avantage : il se restaure en quelques minutes par re-dépôt. Le plan tient en cinq points.

1. **Détection.** Signaux : page modifiée ou défigurée, redirection inattendue, alerte du navigateur « site dangereux », e-mail d'OVH sur une activité anormale, fichiers inconnus vus dans FileZilla. Vérification mensuelle par Moussa : ouvrir le site, comparer la liste des fichiers en ligne avec `www/` local.
2. **Confinement.** Depuis l'espace client OVH : changer le mot de passe FTP, désactiver les utilisateurs FTP inutiles. Ne rien supprimer en ligne avant d'avoir téléchargé une copie de l'état compromis dans un dossier daté (c'est la preuve). Prévenir Yann immédiatement, avant toute autre action.
3. **Éradication et récupération.** Vider le dossier web en ligne, re-déposer `www/` depuis le dépôt git plus le `.htaccess`. Vérifier les en-têtes et les 11 pages. Vérifier dans l'espace client OVH qu'aucune tâche planifiée, aucun utilisateur FTP, aucune redirection de domaine inconnus n'ont été ajoutés.
4. **Communication.** Yann d'abord, toujours. Puis le client par téléphone (pas par un canal qui pourrait être compromis). Toute communication publique revient à Aicha et au fondateur, pas à Sekou.
5. **Post-incident.** Cause racine (mot de passe faible ou réutilisé, poste infecté, compte OVH sans 2FA), mesure correctrice, note d'une page pour l'équipe.

---

## 5. Ce que nous n'avons pas pu vérifier

| Quoi | Pourquoi | Comment le lever |
|---|---|---|
| Que le `.htaccess` est accepté sans erreur 500 par le serveur OVH réel | L'hébergement n'est pas ouvert. Le fichier a été chargé dans un Apache 2.4 local (celui de macOS, modules rewrite, headers, expires, authz) : démarrage sans erreur, six en-têtes servis, fichiers `.md`, `.bak` et `.htaccess` refusés en 403. Non exercés localement : `Options -Indexes` et la redirection HTTPS (serveur de test hors port 80) | Dépôt puis ouverture du site ; en cas d'erreur, retirer les blocs D puis C (procédure dans le fichier) ; tester `/images/` et une adresse en `http://` |
| Les en-têtes réellement servis | Idem | `curl -I https://www.taspalm.com/` après dépôt, sortie envoyée à Sekou |
| L'état du compte OVH du client (2FA, utilisateurs FTP, SFTP activé, SSL coché) | Compte appartenant au client, Sekou ne demande jamais d'accès aux identifiants | Le client vérifie lui-même dans l'espace client, onglets « FTP - SSH » et « Multisite » |
| La licence exacte des deux polices au moment du téléchargement | Page de licence non rouverte dans cet audit | Lire la mention de licence sur la page Google Fonts de chaque police avant de les rapatrier |
| L'étendue des sauvegardes automatiques OVH sur l'offre Perso | Documentation générale, non spécifique à l'offre | Espace client OVH, rubrique de restauration de l'espace de stockage ; ou support OVH |
| Le droit congolais applicable aux données personnelles | Hors compétence de cet audit | Le client se rapproche de son conseil ; le RGPD reste la référence pour les visiteurs en Europe |

---

## 6. Prochaine échéance

- **Re-vérification Sekou** après dépôt du `.htaccess` et du site : lecture des en-têtes servis, test des 11 pages en HTTPS, test de l'adresse `/images/` (doit répondre 403), test d'un fichier `.md` fictif (doit répondre 403). À planifier avec Kofi le jour du dépôt.
- **Passage du HSTS à un an** : une semaine après la mise en ligne, si aucune page ne pose problème en HTTPS.
- **Audit du branchement des formulaires** : avant activation, sur la base des sept exigences du point I-3.
- **Veille** : aucune dépendance logicielle à surveiller (pas de bibliothèque JavaScript, pas de CMS). Point de contrôle trimestriel : fichiers en ligne identiques à `www/`, certificat renouvelé, 2FA toujours active.

---

Récapitulatif pour Kofi :

- **Vérifié** : code propre, sans secret, sans script inline, sans dépendance hors polices, sans métadonnée d'image.
- **À corriger avant mise en ligne** (Moussa) : `.htaccess` déposé et re-vérifié, dépôt limité à `www/` par SFTP.
- **À décider** (client, Kofi) : polices rapatriées ou déclarées ; mentions légales et page Confidentialité remplies.
- **Dépend du client** : SFTP et 2FA sur le compte OVH, mot de passe FTP fort, boîte `contact@taspalm.com` créée, accord des titulaires des numéros publiés.
- **Escaladé** : rien. Aucun point critique.

Sources consultées pour les faits OVH : documentation OVHcloud « Comment activer l'accès SFTP », « Se connecter à l'espace de stockage FTP », « Restaurer l'espace de stockage de son hébergement web », « Sécuriser son compte OVHcloud avec la double authentification », guide « SSL Let's Encrypt » (dépôt ovh/docs), et fils de la communauté OVH sur la redirection HTTPS en `.htaccess`.
