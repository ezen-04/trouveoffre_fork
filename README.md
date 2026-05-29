# trouveoffre (Version 2.0.0)
Le notebook pour trouver des offres et postuler a été remplacé par une architecture modulaire plus élaborée.

🎯 Automatiser sa recherche d'emploi ? Un challenge assez intéressant ! <br>
Un notebook, c'est bien, mais, une architecture solide, c'est encore mieux. C'est pourquoi, la première version du projet **``trouveoffre``** a été améliorer pour cette nouvelle version basé sur une architecture plus élaborée et une manipulabilité beaucoup plus prononcée.

## Architecture

```
assets/
│
├── __init__.py
├── start.py
├── main.py
│
├── core
│   ├── config.py
│   └── auto_config.py
│
├── system
│   └── detect.py
│
├── worker
│   ├── scraper.py
│   └── fichier.py
│
├── db
│   ├── jobs.db     # auto-généré
│   └── session.py
│
├── offres/         # auto-généré
├── .gitignore 
├── requirements.txt
└── README.md
```

## Notes techniques
Vous voulez l'utiliser ? Rien de plus simple ! Il vous suffit de suivre les étapes suivantes:
- Installer Python si cela n'est pas encore fait :
Allez à l'adresse officielle [en cliquant ici](https://www.python.org/downloads/) ou en allant dans votre App store.

- Ouvrez le fichier config se trouvant dans le dossier core, et dans la variable config, veuillez entrer vos préférences en terme d'offre.

- Assurez d'être connecté à internet, ouvrez votre terminal, placez vous dans le dossier où vous avez téléchargé le contenu de ce dépôt, puis exécutez la commande suivante:
```bash
python start.py
```

Le script va s'exécuter tout seul, du début à la fin.

## Améliorations apportées
- Simplicité d'exécution : Plus besoin de manipuler un notebook où en une simple erreur d'attention et de manipulation, tu peux modifier le script et par la suite te retrouver avec des erreurs.

- Architecture modulaire : Beaucoup plus `safe` et facile à maintenir.

- Un proccessus quasi-automatisé: Plus aucun soucis à se faire. Il suffit juste de modifier les critères de recherche dans le fichier config, puis de lancer le fichier start et le tour est joué !