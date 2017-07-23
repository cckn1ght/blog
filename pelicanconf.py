#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Qunhao Song'
SITENAME = u'Pulp Blog'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/Chicago'

DEFAULT_LANG = u'en'

GOOGLE_ANALYTICS = "UA-103006260-1"
THEME = "/Users/qhsong/blog/pure-single"
ARTICLE_EXCLUDES = ['pages']
STATIC_PATHS = ['images', 'gcloud']

TAGLINE = ""
PROFILE_IMG_URL = "images/avatar.jpg"
COVER_IMG_URL = ""


DISPLAY_PAGES_ON_MENU = False

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# metadata generation
DEFAULT_DATE = 'fs'
USE_FOLDER_AS_CATEGORY = True
LOAD_CONTENT_CACHE = False
SUMMARY_MAX_LENGTH = 50

# Blogroll
LINKS = ()

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/qhs0ng'),
          ('github', 'https://github.com/cckn1ght'),)
TWITTER_USERNAME = "qhs0ng"
GITHUB_URL = "https://github.com/cckn1ght/blog"
DISQUS_SITENAME = "the-pulp-blog"

DEFAULT_PAGINATION = 10
PLUGIN_PATHS = ['/Users/qhsong/pelican/pelican-plugins']
PLUGINS = [
    'pelican_gist'
]

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
