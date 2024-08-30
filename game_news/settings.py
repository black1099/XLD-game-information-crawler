BOT_NAME = "game_news"

SPIDER_MODULES = ["game_news.spiders"]
NEWSPIDER_MODULE = "game_news.spiders"

SPIDER_MAX_PAGES = 10

USER_AGENT = "game news"

ROBOTSTXT_OBEY = False

JSON_FILE_NAME = "news.json"


ITEM_PIPELINES = {
   "game_news.pipelines.JsonPipeline": 300,
}

AUTOTHROTTLE_ENABLED = True
AUTOTHROTTLE_TARGET_CONCURRENCY = 1
CONCURRENT_REQUESTS_PER_DOMAIN = 1
DOWNLOAD_DELAY = 1

REQUEST_FINGERPRINTER_IMPLEMENTATION = "2.7"
TWISTED_REACTOR = "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
FEED_EXPORT_ENCODING = "utf-8"