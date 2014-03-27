# -*- coding: utf8 -*-

import sqlite3

class Db:
	def __init__(self, path):
		self.conn = sqlite3.connect(path)
		self.cursor = self.conn.cursor()

	def close(self):
		self.conn.close()

	def execute(self, qr):
		self.cursor.execute(qr)
		self.conn.commit()

	def query(self, qr):
		self.cursor.execute(qr)

		ret = []
		for line in self.cursor:
			ret.append(line)

		return ret
