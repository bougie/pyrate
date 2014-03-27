# -*- coding: utf8 -*-

import smtplib
from email.mime.text import MIMEText

from config import *

class Notif:
	def __init__(self, html=False):
		self.content = ''
		self.html = html

	def add_item(self, title, link):
		if self.html:
			pass
		else:
			if len(self.content) == 0:
				self.content = 'Liste des nouveaux episodes :\n\n'

			self.content = self.content + '    - ' + str(link) + '\n'

	def send(self, sfrom, to, host='localhost'):
		if len(self.content) > 0:
			if DEBUG:
				print
				print self.content
				print

			msg = MIMEText(self.content)
			msg['from'] = sfrom
			msg['to'] = to
			msg['subject'] = '[VOD] Nouveaux episodes gratuits disponibles'

			s = smtplib.SMTP(host)
			s.sendmail(sfrom, [to], msg.as_string())
			s.quit()
