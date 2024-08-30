import scrapy


class GameNewsItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
    time = scrapy.Field()
    image_url = scrapy.Field()
    article_url = scrapy.Field()
    origin = scrapy.Field()