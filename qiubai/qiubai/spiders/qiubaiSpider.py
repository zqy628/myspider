# -*- coding: utf-8 -*-
import scrapy
from qiubai.items import QiubaiItem

class QiubaispiderSpider(scrapy.Spider):
    name = 'qiubaiSpider'
    allowed_domains = ['qiushibaike.com']
    start_urls = []
    for i in xrange(30):
        start_urls.append('https://www.qiushibaike.com/hot/page/' + str(i+2))
    def parse(self, response):
        subSelector = response.xpath("//div[contains(@class,'article block')]")
        items = []
        for sub in subSelector:
            item = QiubaiItem()
            item['author'] = sub.xpath("./div[1]/a[2]/h2/text()").extract()[0]
            item['content'] = sub.xpath(".//div[@class='content']/span//text()").extract()[0]
            if sub.xpath(".//div[@class='thumb']"):
                item['img'] = sub.xpath(".//div[@class='thumb']//@src").extract()[0]
            else:pass
            item['funTimes'] = sub.xpath(".//div[@class='stats']//i[1]/text()").extract()[0]
            item['comments'] = sub.xpath(".//div[@class='stats']//a/i/text()").extract()[0]
            items.append(item)
        return items

