#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHORS = (
    u'Natim',
    u'Meysun'
)
AUTHOR = "C'était trop chou !"

SITENAME = u'C\'était trop chou !'
SITEURL = ''

PATH = 'content'
SUMMARY_MAX_LENGTH = 100
TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'

# Social widget
SOCIAL = (('Github', 'https://github.com/Natim/cttc'),)

DEFAULT_PAGINATION = False

THEME = "pure"

COVER_IMG_URL = '/theme/sidebar.jpg'

SOCIAL = (
    ('envelope', 'mailto:cttc@trunat.fr'),
    ('rss', SITEURL + 'feeds/all.atom.xml'),
    ('github', 'https://github.com/Natim/cttc'),
)

MENUITEMS = (
    ('Archives', 'archives.html'),
    (u'À propos', 'pages/a-propos.html'),
)
STATIC_PATHS = ['images', 'documents', 'extra/CNAME', 'presentations']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['post_stats', 'better_figures_and_images']
RESPONSIVE_IMAGES = True
