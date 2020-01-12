# -*- coding: utf-8 -*-
import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['toscrape.com']
    start_urls = [
            'http://quotes.toscrape.com/page/1/',
            # 'http://quotes.toscrape.com/page/2/',
        ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css('span.text::text').get(),
                'author' : quote.css('small.author::text').get(),
                'tags' : quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page,callback=self.parse)

        # 无需调用urljoin()
        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)

        # You can also pass a selector to response.follow() instead of a string
  #      yield response.follow(response.css('li.next a')[0],callback=self.parse)

