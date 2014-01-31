# -*- coding: utf-8 -*-

import feedparser
import ConfigParser

#rss = "http://rss.voidsec.com/?type=atom10"
config = ConfigParser.RawConfigParser()
config.read("/etc/alan/rss.conf")
allfeed = map(lambda s: s.strip('\''), config.get('feed', 'rssfeed').split(','))


import alan.core.extension as extension
from alan.core.objects.separator import Header, Separator
from alan.core.objects.item import Item
from alan.core.objects.menu import Menu
from alan.core.objects.actions import ExecuteAction

class Extension(extension.Extension):
	
	extensionName = "rss"
	
	# oneslip http://semplice-linux.org 600x800 Semplice-Linux
	
	def generate(self):
		""" Actually generate things. """

		for rss in allfeed:

			feed = feedparser.parse(rss)

			for new in feed['items']:

				self.add(self.return_executable_item(new['title'], new['link'], icon="applications-internet"))


	def return_executable_item(self, label, url, icon=None):
		""" Returns an executable item. """
		
		item = Item(label=label, icon=self.IconPool.get_icon(icon))
		action = ExecuteAction("oneslip %s 800x700 %s" % (url, label))
		item.append(action)
		
		return item