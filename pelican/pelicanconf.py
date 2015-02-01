#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'charlesreid1'
SITENAME = u'This Is Watergate'
SITEURL = '/watergate'

PATH = 'content'

TIMEZONE = 'America/Los_Angeles'

DEFAULT_LANG = u'en'




# --------------8<---------------------

SITETAGLINE = "The President is on the line."

# this image must be in content/images/
SITEIMG = "watergatebkg.jpg" 
IMGVERTOFFSET = "280px"
BLOGTITLE = "On The Horn: The Watergate Twitterbot Blog"



# to install this theme:
# git checkout http://github.com/charlesreid1/coffin-spore-theme
# pelican-themes -i coffin-spore-theme
THEME = 'coffin-spore-theme'




# Don't try to turn HTML files into pages
READERS = {'html': None}

#PLUGIN_PATHS = ['/Users/charles/codes/pelican-plugins/']

STATIC_PATHS = ['images']

DISPLAY_PAGES_ON_MENU = False

TEMPLATE_PAGES = {'blog.html':'blog.html'}



# --------------8<---------------------



# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
