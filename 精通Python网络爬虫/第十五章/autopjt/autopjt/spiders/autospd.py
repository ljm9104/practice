# -*- coding: utf-8 -*-
import scrapy
from autopjt.items import AutopjtItem
from scrapy.http import Request


class AutospdSpider(scrapy.Spider):
    name = 'autospd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://category.dangdang.com/pg1-cid4011029.html']

    def parse(self, response):
        item=AutopjtItem()
        # 通过各Xpath表达式分别提取商品的名称、价格、链接、评论数等信息
        item["name"]=response.xpath("//a[@class='pic']/@title").extract()
        item["price"]=response.xpath("//span[@class='price_n']/text()").extract()
        item["link"]=response.xpath("//a[@class='pic']/@href").extract()
        item["comnum"]=response.xpath("//a[@name='itemlist-review']/text()").extract()

        yield item

        for i in range(1,27):
            url = 'http://category.dangdang.com/pg' + str(i) + '-cid4011029.html'
            yield Request(url, callback=self.parse)
