# -*- coding: utf-8 -*-

import feedparser

import alan.core.extension as extension
from alan.core.objects.separator import Header, Separator
from alan.core.objects.item import Item
from alan.core.objects.menu import Menu
from alan.core.objects.actions import ExecuteAction

class Extension(extension.Extension):
	
	extensionName = "rss"

	def generate(self):
		""" Actually generate things. """
		allfeed = map(lambda s: s.strip('\''), self.extension_settings["rssfeed"].split(','))
		
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