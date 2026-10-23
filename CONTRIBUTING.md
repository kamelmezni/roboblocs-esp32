# Contribuer à RoboBlocs ESP32

Merci de votre intérêt ! Élèves, enseignants et développeurs sont tous les bienvenus.

## Façons de contribuer
- 🐞 **Signaler un bug** (issue « Bug »), en précisant navigateur, système, modèle de carte et version de MicroPython.
- 💡 **Proposer une fonctionnalité** ou un bloc.
- 📚 **Ajouter un exemple** (issue « Nouvel exemple » ou pull request).
- 🌍 **Traduire** l'interface ou le guide.
- 📖 Améliorer la documentation.

## Organisation du code
L'IDE est un **fichier HTML autonome** : `docs/roboblocs.html`.
Il contient la bibliothèque Blockly (minifiée), les définitions de blocs (`type:"..."`, `message0:"..."`),
les générateurs MicroPython, la liste des exemples (`cat:"...",title:"..."`) et les bibliothèques copiées sur la carte (`LIBS.xxx`).

## Marche à suivre
1. *Fork* du dépôt, puis une branche par modification : `git checkout -b ajout-exemple-dht11`.
2. Modifier `docs/roboblocs.html` et ouvrir le fichier dans Chrome ou Edge pour tester.
3. Si possible, tester sur une vraie carte ESP32 (MicroPython).
4. Mettre à jour `CHANGELOG.md` et, pour un exemple, `docs/EXEMPLES.md`.
5. Vérifier les marques d'auteur : `python tools/verifier_marques.py --strict docs/roboblocs.html`.
6. Ouvrir une *pull request* en décrivant ce qui change et comment vous l'avez testé.

## Règles d'un bon exemple
- Un objectif clair, une phrase de description, le matériel et le **schéma de câblage** (broches indiquées).
- Des conseils pas à pas pour l'élève.
- Réutiliser les blocs existants quand c'est possible.
- Prévenir si un composant fonctionne en 5 V (diviseur de tension sur Echo du HC-SR04).

## Attribution
Ne supprimez pas les mentions de copyright ni les marques d'auteur. Les contributeurs sont ajoutés à la liste des
remerciements de chaque version. En contribuant, vous acceptez que votre contribution soit publiée sous licence MIT.

## Conduite
Voir [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
