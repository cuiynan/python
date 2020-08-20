# -*- coding: utf-8 -*-

BOT_NAME = 'ZJPL'

SPIDER_MODULES = ['ZJPL.spiders']
NEWSPIDER_MODULE = 'ZJPL.spiders'

# mysql配置参数
MYSQL_HOST = "172.16.10.157"
MYSQL_PORT = 3306
MYSQL_USER = "root"
MYSQL_PASSWORD = "123456"
MYSQL_DB = 'company_info'
TABLE = "qichacha2"

# # 测试mysql配置参数
# MYSQL_HOST = "localhost"
# MYSQL_PORT = 3306
# MYSQL_USER = "root"
# MYSQL_PASSWORD = "mysql"
# MYSQL_DB = 'company_info'
# TABLE = "qichacha"

# # mongo配置参数
# MONGO_HOST = "172.16.10.175"
# MONGO_PORT = 27017
# MONGO_DB = "gcw_data"
# # MONGO_COL = "gcw"
#
# # redis 配置参数
# REDIS_HOST = "172.16.2.226"
# REDIS_PORT = 9000
# REDIS_PASS = "abc123"
# REDIS_DB = "1"

# redis设置
# REDIS_URL = 'redis://@127.0.0.1:6379'

# 布隆过滤器
BLOOMFILTER_HASH_NUMBER = 6
BLOOMFILTER_BIT = 30

# cookies
COOKIES_URL = 'http://172.16.2.226:5000/gldjc/random'
# log 配置参数
# LOG_ENABLED = True
# LOG_ENCODING = "utf-8"
# LOG_STDOUT = True
# LOG_FILE = "error.log"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 1
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ZJPL.middlewares.ZjplSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
#  'ZJPL.middlewares.ZjplDownloaderMiddleware': 543,
#    'ZJPL.middlewares.CookiesMiddleware': 550,
   'ZJPL.middlewares.RandomUseragentMiddleware': 500,

}

# url去重配置
# DUPEFILTER_CLASS = 'gldjc_detail.duplication.RepeatUrl'
# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
    # 'ZJPL.pipelines.MongoPipeline': 300,
    # 'ZJPL.pipelines.MysqlPipeline': 320,
    # 'ZJPL.pipelines.TuniuPipeline': 200,
    # 'ZJPL.pipelines.RedisPipeline': 310,
# }

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'