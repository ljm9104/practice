# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule

from mycrawlspider.items import MycrawlspiderItem


class WeisuenSpider(CrawlSpider):
    name = 'weisuen'
    allowed_domains = ['sohu.com']
    start_urls = ['http://news.sohu.com/']

    rules = (
        Rule(LinkExtractor(allow=('.*?/n.*?shtml'),allow_domains=('sohu.com')),
            callback='parse_item', follow=True),
            
    )

    def parse_item(self, response):
        i = MycrawlspiderItem()
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        # i['name'] = response.xpath('//div[@id="name"]').extract()
        # i['description'] = response.xpath('//div[@id="description"]').extract()
        #根据Xpath表达式提取新闻网页中的标题
        i["name"]=response.xpath("/html/head/title/text()").extract()
        #根据Xpath表达式提取当前新闻网页的链接
        i["link"]=response.xpath("//link[@rel='canonical']/@href").extract()
        return i
