# -*- coding: utf-8 -*-
import scrapy
from getProxy.items import GetproxyItem

class ProxyspiderSpider(scrapy.Spider):
    name = 'proxySpider'
    allowed_domains = ['proxy360.cn']
    nations = ['Brazil','China','America','Taiwan','Japan','Thailand','Vietnam','bahrein']
    start_urls = []
    for nation in nations:
        start_urls.append('http://www.proxy360.cn/Region/' + nation)

    def parse(self, response):
        subSelector = response.css(".proxylistitem")
        items = []
        for sub in subSelector:
            item = GetproxyItem()
            item['ip'] = sub.xpath("./div/span[1]/text()").extract()[0].strip()
            item['port'] = sub.xpath("./div/span[2]/text()").extract()[0].strip()
            item['type'] = sub.xpath("./div/span[3]/text()").extract()[0].strip()
            item['location'] = sub.xpath("./div/span[4]/text()").extract()[0].strip()
            item['protocol'] = 'HTTP'
            item['source'] = 'proxy360'
            items.append(item)
        return items