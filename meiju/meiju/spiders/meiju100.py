# -*- coding: utf-8 -*-
import scrapy
from meiju.items import MeijuItem

class Meiju100spiderSpider(scrapy.Spider):
	name = "meijuSpider"
	allowed_domains = ["meijutt.com"]
	start_urls = (
		'http://www.meijutt.com/new100.html',
	)

	def parse(self, response):
		subSelector = response.xpath('//*[@id="top-box"]/div[1]/div/div/ul/li')
		items = []
		for sub in subSelector:
			item = MeijuItem()
			item['storyName'] = sub.xpath('./h5/a/text()').extract()[0]
			item['storyState'] = ''.join(sub.xpath('./span[1]//text()').extract())
			item['tvStation'] = sub.xpath('./span[2]/text()').extract()
			item['updateTime'] = sub.xpath('./div[2]//text()').extract()[0]
			items.append(item)
		return items
