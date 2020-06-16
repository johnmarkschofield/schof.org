#!/usr/bin/env python
"""Configuration common to all uses of fab."""
# -*- coding: utf-8 -*- #
from datetime import datetime
import os.path

AUTHOR = u'John Mark Schofield'
SITENAME = u'schof.org'
SITESUBTITLE = u'A journal of learning and doing'
PATH = u'content'

STATIC_PATHS = [
    u'wp-content',
    u'media',
    u'non-media-assets',
    u'galleries',
    u'images']

READERS = {u'html': None}

TIMEZONE = u'America/Los_Angeles'
DEFAULT_LANG = u'en'
THEME = u'gum'  # Clean, easy-to-read. Responsive. Good cat & tag support.

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, u'{name}{number}{extension}', u'{name}{number}{extension}'), )

CURRENT_YEAR = datetime.now().year

DISPLAY_PAGES_ON_MENU = True

PAGE_URL = u'{slug}'
PAGE_SAVE_AS = u'{slug}'

TAG_URL = u'tag/{slug}'
TAG_SAVE_AS = u'tag/{slug}'

TAGS_SAVE_AS = u'tags'

AUTHOR_URL = u''
AUTHOR_SAVE_AS = u''
AUTHORS_SAVE_AS = u''

# AUTHOR_URL = 'author/{slug}'
# AUTHOR_SAVE_AS = 'author/{slug}'
# AUTHORS_SAVE_AS = 'authors'

CATEGORY_URL = u'category/{slug}'
CATEGORY_SAVE_AS = u'category/{slug}'
CATEGORIES_SAVE_AS = u''

ARTICLE_URL = u'{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = u'{date:%Y}/{date:%m}/{date:%d}/{slug}'

YEAR_ARCHIVE_SAVE_AS = u''
MONTH_ARCHIVE_SAVE_AS = u''
ARCHIVES_SAVE_AS = u'archives'

# YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/all'
# MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/all'
# ARCHIVES_SAVE_AS = 'archives'

FEED_DOMAIN = u'https://schof.org'

SLUGIFY_SOURCE = u"basename"

PLUGIN_PATHS = [
    os.path.expandvars(u'$HOME/code/others/pelican-plugins')]

PLUGINS = [u'sitemap', u'simple_footnotes', u'render_math']
# GZIP_CACHE_OVERWRITE = False

SITEMAP = {
    u'format': u'xml',
    u'priorities': {
        u'articles': 1,
        u'indexes': 0.5,
        u'pages': 0.5
    },
    u'changefreqs': {
        u'articles': u'monthly',
        u'indexes': u'daily',
        u'pages': u'monthly'
    }
}


EXTRA_PATH_METADATA = {
    u'non-media-assets/robots.txt': {u'path': 'urobots.txt'},
}

LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = u'mtime'
CACHE_CONTENT = True
