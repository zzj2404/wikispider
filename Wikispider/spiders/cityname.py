import scrapy
import json


class CityNameSpider(scrapy.spiders.Spider):
    name = "cityname"
    start_urls = [
        "https://zh.wikipedia.org/zh-cn/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9F%8E%E5%B8%82%E5%88%97%E8%A1%A8"
    ]

    def parse(self, response):
        names = response.xpath("//div[@class='mw-parser-output']/ul/li/a/text()").extract()
        with open('cityNames.json', 'w') as f:
            json.dump(names, f)
