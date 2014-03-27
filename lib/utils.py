# -*- coding: utf8 -*-

import re

from config import *

def search(filter, data, lang):
	"""
	Recherche l'element filter dans les donnees data.
	Retourne les informations sur l'element recherche ou None en cas d'erreur connue
	"""
	ret = None

	try:
		title = data['title'].decode()
	except:
		title = data['title']

	# On cherche les item qui comporte le filtre dans leur titre
	search_pattern = '.*'.join(filter.split(' '))
	if not re.search(search_pattern, title, flags=re.IGNORECASE) == None:
		# On cherche une langue particuliere
		if not lang == None:
			lang_search_pattern = ".*%s.*" % ('|'.join(lang))
			if re.search(lang_search_pattern, title, flags=re.IGNORECASE) == None:
				return None

		# Recuperation des informations sur l'episode (saison + episode)
		m = re.search('S([0-9]+)E([0-9]+)', title, flags=re.IGNORECASE)
		if not m == None:
			season = m.group(1)
			episode = m.group(2)
		else:
			season = ''
			episode = ''

		ret = {
			'filter': filter,
			'title': title,
			'season': season,
			'episode': episode,
			'date': data['published_parsed'],
			'url': data['link']
		}

		if DEBUG:
			print "DEBUG: %s" % (str(ret))

	return ret
