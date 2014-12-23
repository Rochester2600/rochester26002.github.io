#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'antitree'
SITENAME = u'Rochester 2600'
SITEURL = 'http://rochester2600.github.io'
SITESUBTITLE = "Hacking, Security, Technology meetup group"

THEME = 'pure-single'

PATH = 'content'

STATIC_PATHS = ['images']
COVER_IMG_URL = "/images/2600bg.png"
FAVICON_URL = "/images/favicon.png"


TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Interlock Rochester', 'http://www.interlockroc.org/'),
         )

# Social widget
SOCIAL = (
	('twitter-square', 'https://twitter.com/rochester2600'),
	('google-plus-square', 'https://plus.google.com/+Rochester2600'),
	
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
