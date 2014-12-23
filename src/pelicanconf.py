#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'antitree'
SITENAME = u'Rochester 2600'
SITEURL = 'http://www.rochester2600.com'
SITESUBTITLE = "Hacking, Security, Technology meetup group"

THEME = './theme/pure-single'

PATH = 'content'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}
COVER_IMG_URL = "/images/2600bg.png"
FAVICON_URL = "/images/favicon.png"
SUMMARY_MAX_LENGTH = None


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
	('github-square', 'https://github.com/Rochester2600'),
	
)

DEFAULT_PAGINATION = 3

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
