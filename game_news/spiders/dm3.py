import scrapy
from datetime import datetime
from zoneinfo import ZoneInfo
from ..items import GameNewsItem


class Dm3Spider(scrapy.Spider):
    name = "dm3"
    allowed_domains = ["3dmgame.com"]

    def start_requests(self):
        url = "https://m.3dmgame.com/news/"
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            meta={"page": 1}
        )

    def parse(self, response):
        lis = response.xpath("//div[@class='lis selectpost']")
        for li in lis:
            item = GameNewsItem()
            item["title"] = li.xpath("./div[@class='wp_b']/div/a/text()").get()
            item["article_url"] = li.xpath("./div[@class='wp_b']/div/a/@href").get()
            item["image_url"] = li.xpath("./div[@class='wp_b']/a[@class='img']/img/@data-original").get()
            item["time"] = li.xpath("./div[@class='wp_a']/div[@class='time']/text()").get()
            if "之前" in item["time"]:
                shanghai_zone = ZoneInfo("Asia/Shanghai")
                shanghai_now = datetime.now(shanghai_zone)
                item["time"] = shanghai_now.strftime('%Y-%m-%d')
            item["description"] = None
            item["origin"] = "3dmgame"
            yield item

        page = response.meta["page"] + 1
        url = f'https://m.3dmgame.com/news_all_{page}/'
        if page <= self.settings.get("SPIDER_MAX_PAGES", 20):
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"page": page}
            )