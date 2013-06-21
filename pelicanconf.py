#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Brandon Sandrowicz'
SITENAME = u'Brandon Sandrowicz'
#SITEURL = 'http://brandon.sandrowicz.org'
SITEURL = 'http://localhost:8000'

SITE_LOGO_URL = '/static/images/avatar.jpg'

TIMEZONE = 'America/Toronto'
DEFAULT_LANG = u"en_CA"

TAGLINE = """ Software developer with a focus on web development in Perl and
            Python. """

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

STATIC_PATHS = [ 'pdfs', 'images' ]
THEME = './theme'
MENUITEMS = (
    ("Home", SITEURL),
    ("Resume", SITEURL + "/static/pdfs/BrandonSandrowicz-resume.pdf"),
)

# Blogroll
LINKS =  None

# Social widget
SOCIAL = None

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
