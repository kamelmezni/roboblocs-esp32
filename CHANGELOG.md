# Journal des modifications

Format inspiré de [Keep a Changelog](https://keepachangelog.com/fr/1.1.0/).

## [Non publié]
- Version hors ligne (offline) en préparation.

## [0.5.0] - 2026-10-23
### Ajouté
- Exemple **« Radar de recul + tableau de bord web »** (Wi-Fi) : la carte crée son point d'accès et affiche
  la distance en temps réel, un message d'alerte et une ampoule rouge sous 10 cm.
- Blocs **« tableau de bord web »** (Wi-Fi) et **« buzzer »** (Sons).
- **Fenêtre de démarrage** : annonce de la nouveauté + préparation de l'ESP32 et de MicroPython
  (pilote CP210x, Thonny, installation de MicroPython).
- `tools/verifier_marques.py` : sélecteur de fichier, option `--strict` pour l'intégration continue.

### Modifié
- L'ancienne fenêtre d'accueil (5 étapes d'utilisation) reste accessible via le bouton **❓ Aide**.
