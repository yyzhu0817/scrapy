# -*- coding: utf-8 -*-
import scrapy
# from ..items import TxItem

class TxspiderSpider(scrapy.Spider):
    name = 'txspider'
    allowed_domains = ['tencent.com']
    url = "https://careers.tencent.com/search.html?index="
    offset = 1
    #start_urls 只是最开始的url
    start_urls = [url + str(offset)] #加页数

    def parse(self, response):
        #把431页的URL都给引擎，引擎给调度器去入队列，再给下载器
        for _ in range(1,432):
            yield scrapy.Request(self.url+str(_),\
                                 callback=self.parseHtml)

    def parseHtml(self,response):

        # 每个职位节点对象列表
        base_list = response.xpath('//div[@class="recruit-list"]')

        for base in base_list:
            item = TxItem()
            #item["job"] = base.xpath('./a/h4/text()')是选择器对象, .extract()后成为列表
            item["job"] = base.xpath('./a/h4/text()').extract_first()
            info = base.xpath('./a/p//span/text()').extract()
            item["catogory"] = info[0]
            item["location"] = info[1]
            item["group"] = info[2]
            item["date"] = info[3]

            yield item


