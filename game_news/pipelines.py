import json


class JsonPipeline:
    def __init__(self, file_name):
        self.file_name = file_name

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            file_name=crawler.settings.get("JSON_FILE_NAME", "news.json")
        )

    def open_spider(self, spider):
        self.file = open(self.file_name, "w", encoding="utf-8")

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.file.write(json.dumps(dict(item), ensure_ascii=False) + "\n")
        return item