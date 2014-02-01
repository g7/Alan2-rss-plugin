Alan2 RSS extension
===================
installation
------------
Move rss.py on /usr/share/alan2/alan/extension/rss.py
and edit your /etc/alan/alan.conf like this:

    structure = ItemPool:launcher LauncherPool:launcher - xdgmenu places client-list-menu - Pipe:exaile Pipe:rss - appearance  - Menu:help - logout

    rss_label = RSS
    rss_icon = mail-mark-junk

    [extension:rss]

    rssfeed = 'feed1','feed2','feed3'

after all, run 

	sudo apt-get install python-feedparser
	alan-config -e rss
	openbox --reconfigure

enjoy.
