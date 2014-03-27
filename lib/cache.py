# -*- coding: utf8 -*-

from lib.db import Db

def has_new_item(date):
	"""
	Verifie que le flux a ete mis à jour depuis le dernier traitement.
	La date du dernier traitement est stockee dans un fichier dans CACHE_DIR
	"""
	return True

def add_item(db, filter, title, season, episode, date):
	qr = """
		INSERT INTO feed
		VALUES (
			'%s',
			'%s',
			'%s',
			'%s',
			'%s');
		""" % (filter, title, season, episode, date)

	try:
		db.execute(qr=qr)
	except Exception, e:
		print "ERROR: %s" % (str(e))

def item_exists(db, filter, season, episode):
	qr = """
		SELECT COUNT(*) AS nb
		FROM feed
		WHERE
			filter='%s'
			AND season='%s'
			AND episode='%s';
		""" % (filter, season, episode)

	try:
		res = db.query(qr=qr)

		return res[0][0] > 0
	except Exception, e:
		print "ERROR: %s" % (str(e))

	return False


