import scrapy
from ..items import GameNewsItem


class YouxiaSpider(scrapy.Spider):
    name = "youxia"
    allowed_domains = ["ali213.net"]

    def start_requests(self):
        url = "https://www.ali213.net/news/new/"
        yield scrapy.Request(
            url=url,
            callback=self.parse,
            meta={"page": 1}
        )

    def parse(self, response):
        news = response.xpath(".//div[@class='news_list']/div[@class='n_lone']")
        for i in news:
            item = GameNewsItem()
            item["title"] = i.xpath("./h2/a/text()").get()
            item["article_url"] = i.xpath("./h2/a/@href").get()
            item["description"] = i.xpath("./div[@class='lone_f']/div[@class='lone_f_r']/div[@class='lone_f_r_t']/text()").get()
            item["time"] = i.xpath("./div[@class='lone_f']/div[@class='lone_f_r']/div[@class='lone_f_r_f']/span/text()").get()
            item["image_url"] = i.xpath("./div[@class='lone_f']/div[@class='lone_f_l']/a/img/@src").get()
            item["origin"] = "youxia"
            yield item

        page = response.meta["page"] + 1
        url = f"https://www.ali213.net/news/new/index_{page}.html"
        if page <= self.settings.get("SPIDER_MAX_PAGES", 20):
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                meta={"page": page}
            )