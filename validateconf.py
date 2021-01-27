#!/usr/bin/env python
# -*- coding: utf-8 -*- #
"""Configuration file for validation and debug."""

import os
import sys
sys.path.append(os.curdir)

from commonconf import *  # noqa
from localconf import *  # noqa

# Seems to be broken in python3
PLUGINS.append('w3c_validate')
