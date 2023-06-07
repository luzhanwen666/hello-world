# Scrapy settings for Ajk project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Ajk'

SPIDER_MODULES = ['Ajk.spiders']
NEWSPIDER_MODULE = 'Ajk.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'Ajk (+http://www.yourdomain.com)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 5
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    # 'Accept-Language': 'en',
    'accept-encoding': 'gzip,deflate,br',
    'accept-language': 'zh-CN,zh;q=0.9',
    'cookie': 'aQQ_ajkguid=C383BCF3-9216-71EF-B111-60CBC5894FA4; ajk-appVersion=; seo_source_type=0; id58=CrIcp2OJnqFX5mEvB7X5Ag==; _ga=GA1.2.1425783832.1669967936; isp=true; 58tj_uuid=61591089-665a-45cc-a2c3-1d0747ce9691; als=0; sessid=D59EC0C5-F4A7-407B-BF63-E118FD158035; fzq_h=676e76f3f24744464bb8fe77f558fbdf_1677130885073_a3ce2bd4b5ca4b3fb577a23669750d77_1996123441; _gid=GA1.2.47083810.1677140566; twe=2; xxzl_cid=859a302de1ec452e829a700b67707871; xxzl_deviceid=ZiBi8bGLWE1JYyzZt+qCWVzfISIBCwyffvcmBWIWqJsIzwFulUGE04NMAKY7PJKe; lps=https%3A%2F%2Fcs.zu.anjuke.com%2F%3Ffrom%3DHomePage_TopBar%7Chttps%3A%2F%2Fcs.anjuke.com%2F; new_session=1; init_refer=https%253A%252F%252Fbeijing.anjuke.com%252F; new_uv=3; obtain_by=2; ctid=604; cmctid=7100',
    'referer': 'https://www.baidu.com/',
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'Ajk.middlewares.AjkSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'Ajk.middlewares.UserAgentDownloadMiddleware': 543,
   'Ajk.middlewares.RandomProxy': 542,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'Ajk.pipelines.AjkPipeline_ershoufang': 300,
   'Ajk.pipelines.AjkPipeline_zufang': 301,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
# AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'

# Set settings whose default value is deprecated to a future-proof value
REQUEST_FINGERPRINTER_IMPLEMENTATION = '2.7'
TWISTED_REACTOR = 'twisted.internet.asyncioreactor.AsyncioSelectorReactor'
