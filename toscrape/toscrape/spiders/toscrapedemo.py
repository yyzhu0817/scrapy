# -*- coding: utf-8 -*-
import scrapy


class ToscrapedemoSpider(scrapy.Spider):
    name = 'toscrapedemo'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://toscrape.com/']

    def parse(self, response):
        print(response.text)
