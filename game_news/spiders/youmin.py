import scrapy
import json
from ..items import GameNewsItem


class YouminSpider(scrapy.Spider):
    name = "youmin"
    allowed_domains = ["gamersky.com"]

    def start_requests(self):
        url = 'https://db2.gamersky.com/LabelJsonpAjax.aspx?jsondata={"type":"updatenodelabel", "nodeId":"11007", "page":1}'
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            meta={"page": 1}
        )

    def parse(self, response):
        json_data = json.loads(response.text[1: -2])
        html_content = json_data["body"]
        new_selector = scrapy.selector.Selector(text=html_content)

        for item in new_selector.xpath('//li'):
            game_item = GameNewsItem()
            game_item["title"] = item.xpath('.//a[@class="tt"]/text()').get()
            game_item["article_url"] = item.xpath('.//a[@class="tt"]/@href').get()
            game_item["description"] = item.xpath('.//div[@class="txt"]/text()').get()
            game_item["time"] = item.xpath('.//div[@class="time"]/text()').get()
            game_item["image_url"] = item.xpath('.//img/@src').get()
            game_item["origin"] = "gamersky"
            yield game_item

        page = response.meta["page"] + 1
        url = f'https://db2.gamersky.com/LabelJsonpAjax.aspx?jsondata={{"type":"updatenodelabel", "nodeId":"11007", "page":{page} }}'
        if page <= self.settings.get("SPIDER_MAX_PAGES", 50):
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"page": page}
            )
