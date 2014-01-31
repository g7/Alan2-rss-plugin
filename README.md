Alan2 RSS extension
===================
installation
------------
Move rss.conf on /etc/alan/rss.conf and  
rss.py on /usr/share/alan2/alan/extension/rss.py.
Then edit your /etc/alan/alan.conf like this:

    structure = ItemPool:launcher LauncherPool:launcher - xdgmenu places client-list-menu - Pipe:exaile Pipe:rss - appearance  - Menu:help - logout

    rss_label = RSS
    rss_icon = mail-mark-junk

edit rss.conf with your favorites feeds.
after all, run "openbox --reconfigure""

enjoy.
