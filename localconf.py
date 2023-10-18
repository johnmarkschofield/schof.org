#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""Configuration for building locally."""


import os
import sys
sys.path.append(os.curdir)
from commonconf import *   # pylint: disable=wildcard-import,unused-wildcard-import   # noqa


RELATIVE_URLS = False
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
SITEURL = "http://127.0.0.1:8000"
