# Scrapy settings for cmtFetcher project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import os

BOT_NAME = 'cmtFetcher'

SPIDER_MODULES = ['cmtFetcher.spiders']
NEWSPIDER_MODULE = 'cmtFetcher.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'cmtFetcher (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
# CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
# DOWNLOAD_DELAY = 5

# The download delay setting will honor only one of:
# CONCURRENT_REQUESTS_PER_DOMAIN = 16
# CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
# TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-US;q=0.7',
    'cookie': r'_T_WM=68363135026; XSRF-TOKEN=ca0401; WEIBOCN_FROM=1110006030; MLOGIN=1; M_WEIBOCN_PARAMS=uicode%3D20000174; SUB=_2A25Ng76iDeRhGeNG61QY9CfLwjqIHXVuj8LqrDV6PUJbktANLRnlkW1NS5YCcAq50peJM3nHfWslmbcAl20Iq9vi; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WF-v8bqAxqYfIBhvNGCSFrV5NHD95Qf1h5c1KB4S0.cWs4Dqcj.i--Ri-zciKLsi--ciKLhi-zXdPH_qgvAIs8VMcU09h57eKzc; SSOLoginState=1619513074'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
# SPIDER_MIDDLEWARES = {
#    'cmtFetcher.middlewares.CmtfetcherSpiderMiddleware': 543,
# }

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
    # 'cmtFetcher.middlewares.CmtfetcherDownloaderMiddleware': 543,
    'cmtFetcher.middlewares.ProxyDownloaderMiddleware': 200,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
# EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
# }



# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#    'cmtFetcher.pipelines.CmtfetcherPipeline': 300,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
# AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
# AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
# AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
# AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
# HTTPCACHE_ENABLED = True
# HTTPCACHE_EXPIRATION_SECS = 0
# HTTPCACHE_DIR = 'httpcache'
# HTTPCACHE_IGNORE_HTTP_CODES = []
# HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'


# =========== scrapy-redis ============
# Enables scheduling storing requests queue in redis.
SCHEDULER = "scrapy_redis.scheduler.Scheduler"

# Ensure all spiders share same duplicates filter through redis.
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"

# Enables stats shared based on Redis
STATS_CLASS = "scrapy_redis.stats.RedisStatsCollector"

# Store scraped item in redis for post-processing.
ITEM_PIPELINES = {
    'scrapy_redis.pipelines.RedisPipeline': 300,
    'cmtFetcher.pipelines.MysqlPipeline': 301,
}

REDIS_HOST = os.environ.get('REDIS_HOST', "127.0.0.1")
REDIS_PARAMS = {
    'password': os.environ.get('REDIS_PASSWORD', "123456"),
    "db": 1
}
REDIS_PORT = 6379

MYSQL_HOST = os.environ.get('MYSQL_HOST', "127.0.0.1")
MYSQL_PORT = 3306
MYSQL_USER = 'root'
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', "123456")
MYSQL_DATABASE = 'weibo'

REDIS_COOKIE_LIST_KEY = os.environ.get('REDIS_COOKIE_LIST_KEY', "redis_cookie_list")
