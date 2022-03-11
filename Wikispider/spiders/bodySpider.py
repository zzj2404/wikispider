import scrapy
import json
from urllib.parse import quote, unquote


class bodySpider(scrapy.spiders.Spider):
    name = "bodyspider"
    url_head = "https://zh.wikipedia.org/zh-cn/"
    start_urls = []

    with open('cityNames.json', 'r') as f:
        citylist = json.load(f)
        for city in citylist:
            start_urls.append(url_head + quote(city))

    def parse(self, response):
        tags = response.xpath("//div[@class='mw-parser-output']/h2 | "
                              "//div[@class='mw-parser-output']/h3 | "
                              "//div[@class='mw-parser-output']/p")

        head_1 = unquote(response.url.rsplit('/', 1)[1])
        head_2 = "简介"
        head_3 = ""
        result = []
        content_list = []
        empty_split = ""

        for tag in tags:
            tag_name = tag.xpath("local-name()")[0].extract()
            if tag_name == 'h2':
                if len(content_list) != 0:
                    result.append(self.item_parse(content_list, head_2, head_3))
                content_list.clear()
                head_2 = tag.xpath("./span[@class='mw-headline']/text()")[0].extract()
                head_3 = ""
            elif tag_name == 'h3':
                if len(content_list) != 0:
                    result.append(self.item_parse(content_list, head_2, head_3))
                    content_list.clear()
                head_3 = empty_split.join(tag.xpath("./span[@class='mw-headline']").xpath("./text() | ./a/text()").extract())
            else:
                content_list += tag.xpath("./text() | ./b/text() | ./a/text()").extract()

        if len(content_list) != 0:
            result.append(self.item_parse(content_list, head_2, head_3))

        with open("./cities/" + unquote(head_1) + ".json", 'w') as f:
            json.dump(result, f)

    def item_parse(self, content_list, head_2, head_3):
        empty_split = ""
        if len(head_3) != 0:
            return {"h2": head_2, "h3": head_3, "content": empty_split.join(content_list).replace("\n", "")}
        else:
            return {"h2": head_2, "content": empty_split.join(content_list).replace("\n", "")}


