#!/usr/bin/env python
"""Configuration common to all uses of fab."""
# -*- coding: utf-8 -*- #
from datetime import datetime
import os.path

AUTHOR = 'John Mark Schofield'
SITENAME = 'schof.org'
SITESUBTITLE = 'A journal of learning and doing'
PATH = 'content'
CHECKOUT_DIR = "/srv/schof.org/"

STATIC_PATHS = [
    'non-media-assets',
    'galleries',
    'images']

READERS = {'html': None}

TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = 'en'
THEME = 'gum'  # Clean, easy-to-read. Responsive. Good cat & tag support.

DEFAULT_PAGINATION = 10
DEFAULT_ORPHANS = 2

PAGINATION_PATTERNS = (
    (1, '{url}', '{save_as}'),
    (2, '{name}{number}{extension}', '{name}{number}{extension}'), )

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

FEED_DOMAIN = 'https://schof.org'

SLUGIFY_SOURCE = "basename"

PLUGIN_PATHS = [
    os.path.join(CHECKOUT_DIR, 'pelican-plugins')]

PLUGINS = ['sitemap', 'simple_footnotes', 'render_math', 'photos']
# GZIP_CACHE_OVERWRITE = False

PHOTO_LIBRARY = "/srv/schof.org/content/media"
PHOTO_EXIF_KEEP = True
PHOTO_EXIF_REMOVE_GPS = True
PHOTO_EXIF_COPYRIGHT = "COPYRIGHT"
PHOTO_EXIF_COPYRIGHT_AUTHOR = "John Mark Schofield"


SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.99,
        "indexes": 0.5,
        "pages": 0.99
    },
    "changefreqs": {
        "articles": "daily",
        "indexes": "hourly",
        "pages": "daily"
    }
}


EXTRA_PATH_METADATA = {
    'non-media-assets/robots.txt': {'path': 'urobots.txt'},
}

LOAD_CONTENT_CACHE = True
CHECK_MODIFIED_METHOD = 'mtime'
CACHE_CONTENT = True
