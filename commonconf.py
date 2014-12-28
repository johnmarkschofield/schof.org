#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime

AUTHOR = u'John Mark Schofield'
SITENAME = u'schof.org'
PATH = 'content'

STATIC_PATHS = [
    'wp-content',
    'media',
    'non-media-assets',
    'galleries',
    'images']

READERS = {'html': None}

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'
THEME = 'gum'  # Clean, easy-to-read. Responsive. Good cat & tag support.

DEFAULT_PAGINATION = 10

CURRENT_YEAR = datetime.now().year

DISPLAY_PAGES_ON_MENU = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_SAVE_AS = 'tag/index.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
AUTHORS_SAVE_AS = 'author/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
CATEGORIES_SAVE_AS = 'category/index.html'

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'

FEED_DOMAIN = 'http://schof.org/'

SLUGIFY_SOURCE = "basename"
