# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class Proxyspider2Spider(scrapy.Spider):
    name = 'proxySpider2'
    allowed_domains = ['xicidaili.com']
    types = ['nn','nt','wn','wt']
    start_urls = []
    for tp in types:
        for i in xrange(1,21):
            start_urls.append('http://www.xicidaili.com/'+ tp +'/' + str(i))

    def parse(self, response):
        subSelector = response.xpath("//tr[@class='odd']|//tr[@class='']")
        items = []
        for sub in subSelector:
            item = GetproxyItem()
            item['ip'] = sub.xpath("./td[2]/text()").extract()[0].strip()
            item['port'] = sub.xpath("./td[3]/text()").extract()[0].strip()
            item['type'] = sub.xpath("./td[5]/text()").extract()[0].strip()
            # item['location'] = sub.xpath("./td[4]//text()").extract()[0]
            if sub.xpath("./td[4]/a//text()"):
                item['location'] = sub.xpath("./td[4]/a/text()").extract()[0].strip()
            else:
                item['location'] = sub.xpath("./td[4]/text()").extract()[0].strip()
            item['protocol'] = sub.xpath("./td[6]/text()").extract()[0].strip()
            item['source'] = 'xicidaili'
            items.append(item)
        return items
