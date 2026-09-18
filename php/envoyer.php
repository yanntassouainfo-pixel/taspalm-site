<?php
/* Taspalm · envoi des formulaires du site vers la boîte de l'exploitation.
   Yann Tassoua · 2026-09-18 · règles posées par l'audit sécurité du 17/09/2026 :
   destinataire écrit en dur, validation côté serveur, pot de miel, délai minimal,
   limitation de fréquence, aucun retour à la ligne dans les en-têtes du message. */

declare(strict_types=1);

const DESTINATAIRE = 'societe.taspalm@gmail.com';     // jamais lu depuis le formulaire
const EXPEDITEUR   = 'no-reply@taspalm.com';          // adresse du domaine, exigée par l'hébergeur
const DELAI_MIN    = 3;                               // secondes entre l'affichage et l'envoi
const PAUSE_IP     = 60;                              // secondes entre deux envois d'une même adresse

function sortir(string $page): void { header('Location: ' . $page, true, 303); exit; }
function propre(string $v, int $max): string {
    $v = trim(str_replace(["\r", "\n", "\0"], ' ', $v));   // une seule ligne : pas d'injection d'en-tête
    return mb_substr($v, 0, $max);
}
function texte(string $v, int $max): string {
    $v = trim(str_replace(["\r\n", "\r", "\0"], ["\n", "\n", ''], $v));
    return mb_substr($v, 0, $max);
}

$en      = (($_POST['langue'] ?? 'fr') === 'en');
$base    = $en ? 'en/' : '';
$merci   = $base . 'merci.html';
$erreur  = $base . 'contact.html?envoi=erreur';

if (($_SERVER['REQUEST_METHOD'] ?? '') !== 'POST') { sortir($base . 'contact.html'); }

/* 1. robots : le champ caché doit rester vide, et l'envoi ne peut pas être instantané */
if (($_POST['site_web'] ?? '') !== '') { sortir($merci); }            // on fait croire au robot que c'est parti
$t = (int)($_POST['t'] ?? 0);
if ($t > 0 && (time() - intdiv($t, 1000)) < DELAI_MIN) { sortir($merci); }

/* 2. fréquence : un envoi par minute et par adresse */
$cle = sys_get_temp_dir() . '/taspalm_' . hash('sha256', ($_SERVER['REMOTE_ADDR'] ?? 'x'));
if (is_file($cle) && (time() - (int)@filemtime($cle)) < PAUSE_IP) { sortir($erreur); }

/* 3. champs attendus, selon le formulaire */
$type = propre((string)($_POST['formulaire'] ?? ''), 20);
$champs = [
  'besoin'  => ['produit' => 60, 'usage' => 60, 'volume' => 120, 'pays' => 120, 'contact' => 160],
  'visite'  => ['nom' => 120, 'profil' => 60, 'periode' => 120, 'contact' => 160],
  'contact' => ['nom' => 120, 'contact' => 160],
];
if (!isset($champs[$type])) { sortir($erreur); }

$lignes = [];
foreach ($champs[$type] as $nom => $max) {
    $v = propre((string)($_POST[$nom] ?? ''), $max);
    if ($nom === 'contact' && mb_strlen($v) < 5) { sortir($erreur); }   // seul champ obligatoire partout
    $lignes[] = ucfirst($nom) . ' : ' . ($v === '' ? '(non renseigné)' : $v);
}
$message = texte((string)($_POST['message'] ?? ''), 3000);
if ($type === 'contact' && mb_strlen($message) < 5) { sortir($erreur); }
if ($message !== '') { $lignes[] = ''; $lignes[] = 'Message :'; $lignes[] = $message; }

/* 4. le message */
$titres = ['besoin' => 'Besoin exprimé', 'visite' => 'Demande de visite', 'contact' => 'Message'];
$sujet  = '[taspalm.com] ' . $titres[$type] . ($en ? ' (version anglaise)' : '');
$corps  = $titres[$type] . " reçu depuis le site taspalm.com\n"
        . str_repeat('-', 48) . "\n" . implode("\n", $lignes) . "\n" . str_repeat('-', 48) . "\n"
        . 'Page : ' . propre((string)($_POST['page'] ?? ''), 120) . "\n"
        . 'Date : ' . date('d/m/Y H:i') . " (heure du serveur)\n";

$entetes = [
  'From: Site Taspalm <' . EXPEDITEUR . '>',
  'MIME-Version: 1.0',
  'Content-Type: text/plain; charset=UTF-8',
  'Content-Transfer-Encoding: 8bit',
  'X-Mailer: taspalm.com',
];
$contact = propre((string)($_POST['contact'] ?? ''), 160);
if (filter_var($contact, FILTER_VALIDATE_EMAIL)) { $entetes[] = 'Reply-To: ' . $contact; }

@touch($cle);                                   // la minute d'attente ne démarre qu'à l'envoi réel
$objet = '=?UTF-8?B?' . base64_encode($sujet) . '?=';
$ok = @mail(DESTINATAIRE, $objet, $corps, implode("\r\n", $entetes), '-f' . EXPEDITEUR);
if (!$ok) { $ok = @mail(DESTINATAIRE, $objet, $corps, implode("\r\n", $entetes)); }   // certains hébergeurs refusent -f
sortir($ok ? $merci : $erreur);
