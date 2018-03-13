# -*- coding: utf-8 -*-
from scrapy.spiders import CSVFeedSpider
from mycsv.items import MycsvItem

class MycsvspiderSpider(CSVFeedSpider):
    name = 'mycsvspider'
    allowed_domains = ['iqianyue.com']
    start_urls = ['http://yum.iqianyue.com/weisuenbook/pyspd/part12/mydata.csv']
    headers = ['sex', 'name', 'addr', 'email']
    # 定义间隔符
    # delimiter = ','

    # Do any adaptations you need here
    #def adapt_response(self, response):
    #    return response

    def parse_row(self, response, row):
        i = MycsvItem()
        #i['url'] = row['url']
        #i['name'] = row['name']
        #i['description'] = row['description']
        i['name'] = row['name'].encode()
        i['sex'] = row['sex'].encode()
        print('名字是：', i['name'],'性别是：', i['sex'])
        return i
