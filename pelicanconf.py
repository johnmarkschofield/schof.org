#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'John Mark Schofield'
SITENAME = u'schof.org'
SITEURL = ''
PATH = 'content'
STATIC_PATHS = ['wp-content', 'media', 'non-media-assets']
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
THEME = 'gum'  # Clean, easy-to-read. Responsive. Good cat & tag support.


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = 'atom.xml'
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

CURRENT_YEAR = datetime.now().year

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
DISPLAY_PAGES_ON_MENU = True
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
