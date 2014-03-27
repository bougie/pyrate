# PYRATE
Pyrate est un script permettant de suivre des fluxs RSS de series et de notifier lors de la sortie de nouveaux épisodes.

# Installation
## Dependances
Pyrate depend de la bibliotheque feedparser et de sqlite3.

Pour l'installation, rien de plus simple :
```
# pip install feedparser
# pip install sqlite3
```

## Recuperation des sources
Cloner ensuite les sources dans un dossier.

## Configuration
Pour configurer pyrate :
```
# cp config.sample.py config.py
# vi config.py
```

# Utilisation

Il suffit de lancer le script main.py :
```
# python main.py
```

Mettre ce script en crontab pour automatiser les traitements.
