# -*- coding: utf8 -*-

import sys
import feedparser
import os

from config import *
from lib.db import Db
from lib.utils import *
from lib.cache import *
from lib.notif import *

if __name__ == "__main__":
	if len(FEED_URL) == 0:
		sys,exit(1)

	if not os.path.isfile(DB_FILE):
		print "ERROR: you need to execute install script"
		sys.exit(1)

	db = Db(path=DB_FILE)

	#
	# On recupere la liste des nouveaux episodes pour la liste des series suivies
	#
	results= []
	feed = feedparser.parse(FEED_URL)
	for item in feed['items']:
		try:
			if has_new_item(item['published_parsed']):
				if DEBUG:
					print "DEBUG: %s" % (item['title'])

				for filter in FILTERS:
					item_result = search(filter=filter['title'], data=item, lang=LANG)

					if not item_result == None and item_exists(db=db, filter=filter['title'], season=item_result['season'], episode=item_result['episode']) == False:
						results.append(item_result)
						break
		except UnicodeError, e:
			pass
		except Exception, e:
			print "Error while parsing feed results : %s" % (str(e))

	#
	# Traitement des nouveaux episodes
	#
	notif = Notif()
	for item in results:
		if DEBUG:
			print "DEBUG: traitement de '%s S%sE%s'" % (item['filter'], item['season'], item['episode'])

		notif.add_item(title=item['title'], link=item['url'])

		add_item(
			db=db,
			filter=item['filter'],
			title=item['title'],
			season=item['season'],
			episode=item['episode'],
			date=item['date'])

	if 'host' in SMTP:
		notif.send(sfrom=SMTP['from'], to=SMTP['to'], host=SMTP['host'])
	else:
		notif.send(sfrom=SMTP['from'], to=SMTP['to'])
