from datetime import datetime

AUTHOR = 'Chinmay Badjatya'
SITEURL = 'http://localhost:8000'
SITENAME = 'Chinmay Badjatya'
SITETITLE = 'Chinmay Badjatya'
SITESUBTITLE = 'Software Developer'
SITEDESCRIPTION = 'Software Developer'
# SITELOGO = ''
# FAVICON = '/images/favicon.ico'
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'

ROBOTS = 'index, follow'

THEME = 'Flex'
PATH = 'content'
OUTPUT_PATH = 'blog/'
TIMEZONE = 'Asia/Kolkata'

I18N_TEMPLATES_LANG = 'en'
DEFAULT_LANG = 'en'
OG_LOCALE = 'en_US'
LOCALE = 'en_US'

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True

SOCIAL = (
    ('github', 'https://github.com/Chinmay4400'),
    ('linkedin', 'https://www.linkedin.com/in/chinmay-badjatya-675a10162/'),
    ('twitter', 'https://twitter.com/ChinmayBadjatya'),
)

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "flex-pelican"
ADD_THIS_ID = 'ra-55adbb025d4f7e55'

STATIC_PATHS = ['images', 'extra/ads.txt']
EXTRA_PATH_METADATA = {'extra/ads.txt': {'path': 'ads.txt'},}

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
