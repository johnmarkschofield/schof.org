#!/usr/bin/env python
"""Configuration common to all uses of fab."""
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from datetime import datetime
import os.path

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
DEFAULT_ORPHANS = 2

# PAGINATION_PATTERNS = (
#     (1, '{base_name}/', '{base_name}/index.html'),
#     (2, '{base_name}/page/{number}', '{base_name}/page/{number}/index.html'),
# )

PAGINATION_PATTERNS = (
    (0, u'{name}{number}{extension}', u'{name}{number}{extension}'), )

CURRENT_YEAR = datetime.now().year

DISPLAY_PAGES_ON_MENU = True

PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}'

TAGS_SAVE_AS = 'tags'

AUTHOR_URL = ''
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

# AUTHOR_URL = 'author/{slug}'
# AUTHOR_SAVE_AS = 'author/{slug}'
# AUTHORS_SAVE_AS = 'authors'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}'
CATEGORIES_SAVE_AS = ''

ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}'

YEAR_ARCHIVE_SAVE_AS = ''
MONTH_ARCHIVE_SAVE_AS = ''
ARCHIVES_SAVE_AS = 'archives'

# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/all'
# MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/all'
# ARCHIVES_SAVE_AS = 'archives'

FEED_DOMAIN = 'https://schof.org/'

SLUGIFY_SOURCE = "basename"

PLUGIN_PATHS = [
    os.path.expandvars('$HOME/code/me/pelican-plugins')]

PLUGINS = ['sitemap', 'simple_footnotes', 'render_math']
# GZIP_CACHE_OVERWRITE = False

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 1,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}


EXTRA_PATH_METADATA = {
    'non-media-assets/robots.txt': {'path': 'robots.txt'},
}

LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CACHE_CONTENT = True
