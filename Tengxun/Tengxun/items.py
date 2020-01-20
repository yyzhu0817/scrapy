# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


# 定义要爬取的数据结构
class TengxunItem(scrapy.Item):
    # 职位名称
    zhName = scrapy.Field()

    # 事业群
    group = scrapy.Field()

    # 工作地点
    zhAddress = scrapy.Field()

    # 职位类别
    zhType = scrapy.Field()

    # 发布时间
    zhTime = scrapy.Field()
