# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class GetproxyPipeline(object):
    filename = 'proxy.txt'
    def process_item(self, item, spider):
        with open(self.filename,'a') as fp:
            fp.write(item['ip'].encode('utf8') + '\t')
            fp.write(item['port'].encode('utf8') + '\t')
            fp.write(item['protocol'].encode('utf8') + '\t')
            fp.write(item['type'].encode('utf8') + '\t')
            fp.write(item['location'].encode('utf8') + '\t')
            fp.write(item['source'].encode('utf8') + '\n')
        return item

