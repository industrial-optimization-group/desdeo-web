#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Frankie Robertson'
SITENAME = 'DESDEO'
SITEURL = 'https://desdeo.it.jyu.fi/'

PATH = 'content'

TIMEZONE = 'Europe/Helsinki'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "."

MENUITEMS = [
  ('Home', '/'),
  ('About', '/pages/about-desdeo.html'),
  ('Source code', 'https://github.com/industrial-optimization-group/DESDEO'),
  ('Documentation', 'https://desdeo.readthedocs.io/'),
]
