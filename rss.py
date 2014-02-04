# -*- coding: utf-8 -*-

import os
import feedparser
import urllib2

import alan.core.extension as extension
from alan.core.objects.separator import Header, Separator
from alan.core.objects.item import Item
from alan.core.objects.menu import Menu
from alan.core.objects.actions import ExecuteAction

CACHE = os.path.expanduser("~/.config/alan-rss/")
if not os.path.exists(CACHE): os.makedirs(CACHE)

class Extension(extension.Extension):
	
	extensionName = "rss"
	
	def sanitize_link(self, link):
		""" Sanitizes the link. """

		return link.replace(":","_").replace("/","_")

	def generate(self):
		""" Actually generate things. """

		for _id in self.extension_settings["structure"].split(" "):
			self.add(self.generate_menu(_id))
		
	def generate_menu(self, _id):
		""" Generates a submenu. """
		
		count = 0
		menu = Menu("rss_%s" % _id, label=self.extension_settings["%s_label" % _id], icon=self.IconPool.get_icon("gtk-directory"))
		
		for feed in self.extension_settings["%s_feeds" % _id].split(" "):
			try:
				count += 1
				
				feed = feedparser.parse(feed)
				
				if "icon" in feed.feed:
					try:
						icon = os.path.join(CACHE, self.sanitize_link(feed.feed.link))
						if not os.path.exists(icon):
							with open(sanitized, "wb") as f:
								i = urllib2.urlopen(feed.feed.icon)
								f.write(i.read())
								i.close()
					except:
						pass
				else:
					icon = self.IconPool.get_icon("applications-internet")
				
				# Feed menu
				feed_menu = Menu("rss_%s_%s" % (_id, count), label=feed.feed.title, icon=icon)
				
				for new in feed.entries:
					feed_menu.append(self.return_executable_item(new['title'], new['link'], icon=icon))
				
				menu.append(feed_menu)
			except:
				pass
		
		return menu

	def return_executable_item(self, label, url, icon=None):
		""" Returns an executable item. """
		
		item = Item(label=label, icon=icon)
		action = ExecuteAction("x-www-browser %s" % url)
		item.append(action)
		
		return item
