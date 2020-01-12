# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from . import settings
# from spiders.txspider import TxspiderSpider
class TxPipeline(object):
    def process_item(self, item, spider):
        print('='*30)
        print(item["job"])
        print(item["catogory"])
        print(item["location"])
        print(item["group"])
        print(item["date"])
        print('='*30)
