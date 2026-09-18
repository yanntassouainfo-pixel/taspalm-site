# Taspalm · site « L'Exploitation »

Site statique bilingue (FR / EN) de l'exploitation agricole Taspalm, Ibenga, Likouala, République du Congo.
Conception et développement : Yann Tassoua, septembre 2026.

## Structure

- `www/` : le site prêt à déposer sur l'hébergement (FTP / SFTP), `.htaccess` compris. C'est ce dossier, et lui seul, qui va sur le serveur.
- `build.py` : le générateur. Toute modification se fait ici, jamais dans `www/` à la main.
- `traductions_en.py` : le dictionnaire français → anglais. Un texte français sans équivalent est signalé à la construction.
- `images-source/` : les visuels d'origine (PNG), convertis en JPEG par le générateur.
- `fonts/` : Cormorant Garamond et Manrope, hébergées sur le site (aucun appel externe).
- `render.py`, `render_en.py` : rendus pleine hauteur pour contrôle visuel.
- `AUDIT-SECURITE_Sekou_2026-09-17.md`, `htaccess-recommande.txt` : audit et durcissement.

## Reconstruire

```bash
python3 build.py
```

Dépendances : Python 3, Pillow.

## État

Les photographies sont des images d'illustration en attente des prises de vue sur le domaine. Les valeurs entre crochets sont des emplacements à remplir par l'exploitation. Les formulaires ne sont pas encore branchés.
