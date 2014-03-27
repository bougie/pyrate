# -*- coding: utf8 -*-

from lib.db import Db

def install(path):
	db_create_qr = """
		CREATE TABLE feed (
			filter TEXT,
			name TEXT,
			season TEXT,
			episode TEXT,
			date TEXT
		);
	"""

	db = Db(path=path)
	try:
		db.execute(db_create_qr)
	except Exception, e:
		print "ERROR: %s" % (str(e))
		sys.exit(1)

if __name__ == "__main__":
	from config import *
	install(path=DB_FILE)
