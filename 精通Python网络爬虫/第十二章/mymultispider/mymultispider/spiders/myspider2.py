# -*- coding: utf-8 -*-
import scrapy


class Myspider2Spider(scrapy.Spider):
    name = 'myspider2'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://sina.com.cn/']

    def parse(self, response):
        pass
