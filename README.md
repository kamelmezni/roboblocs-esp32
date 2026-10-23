<div align="center">

# 🤖 RoboBlocs ESP32

**Programmer une carte ESP32 par blocs, directement dans le navigateur. Sans installation, sans compte, gratuit.**

[▶ Ouvrir l'IDE](https://VOTRE-COMPTE.github.io/roboblocs-esp32/roboblocs.html) ·
[📖 Guide](https://VOTRE-COMPTE.github.io/roboblocs-esp32/ide.html) ·
[📚 Exemples](docs/EXEMPLES.md) ·
[🗺️ Feuille de route](ROADMAP.md)

![Licence MIT](https://img.shields.io/badge/licence-MIT-green)
![Statut](https://img.shields.io/badge/statut-phase%20de%20test-orange)
![Plateforme](https://img.shields.io/badge/ESP32-MicroPython-blue)
![Navigateur](https://img.shields.io/badge/Chrome%20%2F%20Edge-Web%20Serial-lightgrey)

*Un projet du Club Internet des Objets et IA, Lycée Liberté Jendouba (Tunisie), par Prof. MEZNI Kamel.*

</div>

---

## ✨ Pourquoi RoboBlocs ?

Les cartes ESP32 sont idéales pour apprendre l'électronique et l'Internet des Objets, mais leur prise en main
(IDE, câbles, code, bibliothèques) décourage vite les débutants. RoboBlocs propose :

- 🧩 **Programmation par blocs** (style Scratch) basée sur [Blockly](https://github.com/google/blockly), qui génère du **MicroPython** lisible.
- 🔌 **Connexion USB depuis le navigateur** (Web Serial) : envoyer, lancer, arrêter, et même « mettre sur la carte » pour un démarrage autonome.
- 📶 **Wi-Fi intégré** : serveur web, point d'accès sans box, **QR code** pour rejoindre le réseau, **tableau de bord web** en temps réel.
- 📡 **Capteurs et actionneurs** : LED, servo-moteur, ultrason HC-SR04, buzzer, bouton, Bluetooth BLE…
- 🏫 **Pensé pour la classe** : interface en français, exemples prêts à l'emploi, fonctionne hors connexion internet une fois la page chargée.
- 📦 **Un seul fichier HTML autonome** : facile à copier sur une clé USB, à héberger ou à modifier.

## 🆕 Nouveauté 0.5.0 : Radar de recul + tableau de bord Wi-Fi

La carte crée son Wi-Fi et sert une page web (avec le logo du club) qui affiche la **distance en temps réel**,
un **message d'alerte** et une **ampoule rouge** quand un obstacle est à moins de 10 cm, en plus de la LED et du
buzzer. Voir [docs/EXEMPLES.md](docs/EXEMPLES.md).

## 🚀 Démarrage rapide

### 1. Préparer la carte (une seule fois)
1. Installer le pilote **CP210x** : <https://www.silabs.com/developer-tools/usb-to-uart-bridge-vcp-drivers>
2. Installer **[Thonny](https://thonny.org)**.
3. Brancher l'ESP32 avec un câble USB qui transmet les données.
4. Dans Thonny : *Exécuter → Configurer l'interpréteur* → **MicroPython (ESP32)** → *Installer ou mettre à jour MicroPython*.
5. **Fermer Thonny** : le port USB ne peut servir qu'à un seul logiciel à la fois.

### 2. Programmer
1. Ouvrir `roboblocs.html` avec **Chrome ou Edge** (Web Serial n'existe pas sous Firefox ni Safari).
2. **🔌 Connecter la carte** et choisir le port (CP210x).
3. Assembler les blocs, ou charger un modèle avec **📚 Exemples**.
4. **▶ Envoyer et lancer**. Pour un démarrage autonome : **📲 Mettre sur la carte**.

### 3. Lancer en local
```bash
git clone https://github.com/kamelmezni/roboblocs-esp32.git
cd roboblocs-esp32/docs
python -m http.server 8000      # puis ouvrir http://localhost:8000/roboblocs.html
```
Double-cliquer sur `docs/roboblocs.html` fonctionne aussi.

## 🗂️ Structure du dépôt

```
roboblocs-esp32/
├── docs/                    Site GitHub Pages
│   ├── index.html           Page d'accueil du projet
│   ├── roboblocs.html       L'IDE (fichier autonome)
│   ├── ide.html             Guide d'utilisation
│   └── EXEMPLES.md          Catalogue des exemples et montages
├── examples/                Projets .json partagés par la communauté
├── tools/verifier_marques.py  Vérifie les marques d'auteur d'un fichier
├── .github/                 Modèles d'issues, PR et automatisations
├── CHANGELOG.md · ROADMAP.md · CONTRIBUTING.md
└── LICENSE · THIRD_PARTY_NOTICES.md
```

## 🤝 Contribuer

Les contributions sont bienvenues : nouveaux exemples, blocs, traductions, corrections, retours d'élèves et
d'enseignants. Lire [CONTRIBUTING.md](CONTRIBUTING.md), puis ouvrir une *issue* ou une *pull request*.

## 🔐 Attribution et intégrité

Le code est sous **licence MIT** : vous pouvez l'utiliser, le modifier et le redistribuer, à condition de **conserver
la mention de copyright**. Le fichier contient des marques d'auteur visibles et une empreinte invisible ;
`tools/verifier_marques.py` permet de les contrôler. Détails dans [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md).

## 📬 Contact

Prof. MEZNI Kamel · Lycée Liberté Jendouba · <kamel.mezni@gmail.com>

---

## 🌍 English summary

**RoboBlocs ESP32** is a free, single-file, browser-based block-programming IDE for the ESP32 (Blockly → MicroPython,
USB via Web Serial in Chrome/Edge). It includes Wi-Fi web servers, access-point mode with QR codes, a live web
dashboard, BLE, ultrasonic sensor, servo and buzzer blocks. Open `docs/roboblocs.html` in Chrome or Edge. MIT licensed;
status: testing phase. Built for classrooms by the IoT & AI Club, Lycée Liberté Jendouba, Tunisia.
