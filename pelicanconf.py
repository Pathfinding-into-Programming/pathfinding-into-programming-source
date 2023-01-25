AUTHOR = "Aditya Jyoti"
SITENAME = "Pathfinding Into Programming"
SITEURL = ""
PATH = "content"
TIMEZONE = "Asia/Calcutta"
DEFAULT_LANG = "English"

# main site
SUBTITLE = "Pathfinding Into Programming"
SUBTEXT = """
This is an experiment to try and learn the basics about multiple 
programming languages to find my most favorite one, named Project 
<strong>Pathfinding Into Programming</strong>. By the end of this 
project I would have hoped to have learnt the basics about at least 
7 new programming languages other than the one I am already familiar 
with, that being <a class='underline' href='https://en.wikipedia.org/wiki/Python_(programming_language)'>Python</a>.
<br><br>
For this experiment I will be coding up the <a class='underline' 
href='https://en.wikipedia.org/wiki/A*_search_algorithm'>A* 
Pathfinding Algorithm</a> in every language that I decide to try
out. There is no fixed time constraint that I am limiting myself 
to but I will hopefully have tried out atleast one language per month.
<br><br>
You can find the source code to this website <a class='underline' 
href='https://github.com/Reverend-Toady/pathfinding-into-programming'>
here</a>
"""

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Pelican Papyrus stuff
THEME = "themes/Papyrus"
THEME_STATIC_PATHS = ["static"]
PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["readtime", "neighbors", "pelican-toc"]

DISPLAY_PAGES_ON_MENU = True
DIRECT_TEMPLATES = (
    "index",
    "search",
    "tags",
    "categories",
    "archives",
)
PAGINATED_TEMPLATES = {
    "index": None,
    "tag": None,
    "category": None,
    "author": None,
    "archives": 24,
}
# Table of Content Plugin
TOC = {
    "TOC_HEADERS": "^h[1-3]",
    "TOC_RUN": "true",
    "TOC_INCLUDE_TITLE": "false",
}

# Blogroll
LINKS = (("reddit", "https://reddit.com/submit?url="),)

# Social widget
SOCIAL = (
    ("github", "https://github.com/Reverend-Toady"),
    ("discord", "https://discordapp.com/users/593036316980019220"),
    ("google", "mailto:rev.toady.py@gmail.com"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
