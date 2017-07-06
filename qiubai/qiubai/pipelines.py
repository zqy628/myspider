# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from pymongo import MongoClient

class QiubaiPipeline(object):
    client = MongoClient('localhost', 27017)
    db = client.qiushi

    def process_item(self, item, spider):
        self.db.jokes.insert_one(dict(item)).inserted_id
        return item

