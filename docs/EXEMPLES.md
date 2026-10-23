# Catalogue des exemples

Exemples disponibles dans le bouton **📚 Exemples** de l'IDE. Ce fichier est généré à partir de `docs/roboblocs.html`.

## Clignoter la LED

**Catégorie :** Lumières

La LED intégrée (broche 2) s'allume 0,5 seconde puis s'éteint 0,5 seconde, sans fin.

## Servo-moteur va-et-vient

**Catégorie :** Mouvement

Le servo tourne à 0°, 90° puis 180°, en boucle.

**Montage et conseils**

- Fil signal du servo sur la broche 13, rouge sur 5V (VIN), marron/noir sur GND.

## Clignoter 5 fois puis s'arrêter

**Catégorie :** Contrôle

Le bloc « répéter » joue une séquence un nombre précis de fois.

## Bouton → LED

**Catégorie :** Capteurs

Tant que tu appuies sur le bouton BOOT de la carte (broche 0), la LED est allumée.

## Mesurer une distance

**Catégorie :** Capteurs

Affiche la distance mesurée par le capteur ultrason dans la console.

**Montage et conseils**

- HC-SR04 : Trig sur la broche 23, Echo sur la broche 22 (avec un diviseur de tension), VCC sur 5V (VIN), GND sur GND.

## Alarme de proximité

**Catégorie :** Opérateurs

Le capteur ultrason mesure la distance : la LED (broche 21) s'allume si un objet est à moins de 10 cm, sinon elle reste éteinte.

**Montage et conseils**

- HC-SR04 : Trig sur la broche 23, Echo sur la broche 22 (avec un diviseur de tension), VCC sur 5V (VIN), GND sur GND.
- LED : patte longue (+) sur la broche 21 via une résistance de 220 Ω, patte courte (−) sur GND.
- Approche ta main à moins de 10 cm du capteur : la LED s'allume. Le test « ≥ 0 » évite d'allumer la LED quand le capteur ne reçoit aucun écho (valeur -1).

## Radar de recul (alarme de parking)

**Catégorie :** Sons

Comme un radar de recul de voiture : sous 10 cm, la LED (broche 21) s'allume et le buzzer (broche 19) fait des bips de plus en plus rapides quand l'obstacle se rapproche.

**Montage et conseils**

- HC-SR04 : Trig sur la broche 23, Echo sur la broche 22 (avec un diviseur de tension), VCC sur 5V (VIN), GND sur GND.
- LED : patte longue (+) sur la broche 21 via une résistance de 220 Ω, patte courte (−) sur GND.
- Buzzer actif : fil (+) sur la broche 19, fil (−) sur GND.
- Approche ta main du capteur : plus elle est proche, plus les bips sont rapides. Pause entre 2 bips = distance × 0,03 s.

## Radar de recul + tableau de bord web 🆕

**Catégorie :** Wi-Fi

Amélioration du radar de recul : la carte crée son Wi-Fi et affiche un tableau de bord web (logo du club) avec la distance en temps réel, un message d'alerte et une ampoule qui s'allume en rouge sous 10 cm. LED et buzzer fonctionnent comme avant.

**Montage et conseils**

- Même montage que le radar de recul : HC-SR04 (Trig 23, Echo 22 avec diviseur de tension, VCC 5V), LED sur la broche 21, buzzer actif sur la broche 19.
- Clique sur « Envoyer et lancer ». Le bouton « QR code » affiche le code pour rejoindre le Wi-Fi ESP32-Radar (mot de passe 12345678), puis celui de la page.
- Connecte ton téléphone ou ton PC au Wi-Fi ESP32-Radar et ouvre http://192.168.4.1 dans le navigateur.
- Approche la main du capteur : la distance change en temps réel ; sous 10 cm, le message d'alerte apparaît et l'ampoule devient rouge.
- Pour utiliser ta box à la place : remplace le bloc « créer un Wi-Fi » par « se connecter au Wi-Fi » et ouvre l'adresse IP affichée dans la console.

## Compteur

**Catégorie :** Variables

Une variable « compteur » augmente de 1 chaque seconde et s'affiche dans la console.

## Serveur web : allumer / éteindre la LED

**Catégorie :** Wi-Fi

La carte se connecte à ta box et affiche une page web avec 2 boutons pour commander la LED (broche 2).

**Montage et conseils**

- Remplace NOM_DU_WIFI et MOT_DE_PASSE par ceux de ta box (Wi-Fi 2,4 GHz).
- Clique sur « Envoyer et lancer » et lis l'adresse IP dans la console (ex : 192.168.1.20).
- Sur un téléphone ou PC connecté au même Wi-Fi, ouvre cette adresse dans le navigateur.
- Clique sur ALLUMER / ÉTEINDRE.

## Serveur web sans box (point d'accès)

**Catégorie :** Wi-Fi

La carte crée son propre réseau Wi-Fi. Pratique en classe, sans connexion internet.

**Montage et conseils**

- Clique sur « Envoyer et lancer ».
- Sur le téléphone, connecte-toi au Wi-Fi « ESP32-Robo » (mot de passe 12345678).
- Ouvre http://192.168.4.1 dans le navigateur (garde le Wi-Fi même s'il dit « pas d'internet »).
- Clique sur ALLUMER / ÉTEINDRE.

## Serveur web avec QR code (sans taper d'adresse)

**Catégorie :** Wi-Fi

Comme le point d'accès, mais les élèves scannent un QR code pour rejoindre le Wi-Fi puis un second pour ouvrir la page. Aucune adresse IP à taper.

**Montage et conseils**

- Clique sur « Envoyer et lancer ».
- Clique sur le bouton « 📱 QR code » en haut : 2 codes s'affichent (tu peux les projeter au tableau).
- Élève : scanne le code 1 avec l'appareil photo du téléphone pour rejoindre le Wi-Fi « ESP32-Robo ».
- Puis scanne le code 2 pour ouvrir la page (http://192.168.4.1) et clique sur ALLUMER / ÉTEINDRE.

## LED par Bluetooth BLE (Android)

**Catégorie :** Bluetooth

Envoie 1 ou 0 depuis l'application « Serial Bluetooth Terminal » pour allumer ou éteindre la LED (broche 2). Même principe que l'activité 08.

**Montage et conseils**

- Installe « Serial Bluetooth Terminal » (Kai Morich) sur Android ; active le Bluetooth (et la localisation si demandé).
- Clique sur « Envoyer et lancer » : la console affiche « Bluetooth prêt : ESP32-LED ».
- Dans l'application : menu ☰ → Devices → onglet « Bluetooth LE » (pas Classic) → SCAN → touche ESP32-LED.
- Appuie sur l'icône de prise pour te connecter, écris 1 puis envoie : la LED s'allume. Écris 0 : elle s'éteint.
