# -*- coding: utf-8 -*-
import scrapy


class AuthorSpiderSpider(scrapy.Spider):
    name = 'author_spider'
    allowed_domains = ['toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):

        for href in response.css('.author + a::attr(href)'):
            yield response.follow(href,self.parse_author)

        for href in response.css('li.next a::attr(href)'):
            yield response.follow(href,self.parse)


    def parse_author(self,response):
        yield {
            'name': response.css('h3.author-title::text').get(default='').strip(),
            'birthdate':response.css('.author-born-date::text').get(default='').strip(),
            'bio': response.css('div.author-description::text').get(default='').strip()
        }