import os, sys
from scrapy import cmdline

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# cmdline.execute(['scrapy', 'crawl', 'weisuen'])


cmdline.execute('scrapy crawl weisuen'.split())