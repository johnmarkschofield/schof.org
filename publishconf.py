#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import os
import sys
sys.path.append(os.curdir)
from commonconf import *  # noqa

RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = None
FEED_ATOM = None
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
TAG_FEED_ATOM = None
TAG_FEED_RSS = None

FEED_MAX_ITEMS = 99

SITEURL = 'https://schof.org'
