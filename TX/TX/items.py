# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TxItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    job = scrapy.Field()
    catogory = scrapy.Field()
    location = scrapy.Field()
    group = scrapy.Field()
    date = scrapy.Field()
