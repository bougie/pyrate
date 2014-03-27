# -*- coding: utf8 -*-

import os

# URL du flux RSS
FEED_URL = ""

# Liste des episodes à suivre
FILTERS = [
	#{'title': 'nom de la serie'}
]
# Langue(s) (VO, VF, VOSTFR, ...) ou None dans le cas ou pas de filtre sur la langue
LANG = ['VOSTFR']

# Parametre utilisé pour envoyer un mail
SMTP = {
	'host': '', # Serveur SMTP
	'from': '', # Adresse email de l'expediteur (sans reelle importance)
	'to': ''    # Adresse vers laquelle envoyer les notifications
}

# Afficher ou non les lignes de debug du script
DEBUG = False

# Dossier contenant les les fichiers de cache (par default le repertoire du script)
CACHE_DIR = os.getcwd()

# Fichier de la base de données des episodes traites (par default correspond au CACHE_DIR + db.sqlite)
DB_FILE = os.path.join(CACHE_DIR, 'db.sqlite')
