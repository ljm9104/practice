# -*- coding: utf-8 -*-
from scrapy.spiders import XMLFeedSpider
from myxml.items import MyxmlItem

class MyxmlspiderSpider(XMLFeedSpider):
    name = 'myxmlspider'
    allowed_domains = ['sina.com.cn']
    start_urls = ['http://rss.sina.com.cn/roll/sports/hot_roll.xml']
    iterator = 'iternodes' # you can change this; see the docs
    itertag = 'rss' # change it accordingly

    def parse_node(self, response, node):
        i = MyxmlItem()
        #利用XPath表达式将对应信息提取出来，并存储到对应的Item中
        i['title'] = node.xpath("/rss/channel/item/title/text()").extract()
        i['link'] = node.xpath("/rss/channel/item/link/text()").extract()
        i['author'] = node.xpath("/rss/channel/item/author/text()")
        #通过for循环以此遍历出提取出来存在item中的信息并输出
        for j in range(len(i['title'])):
            print("第"+str(j+1)+"篇文章")
            print("标题是：")
            print(i['title'][j])
            print("对应链接是：")
            print(i['link'][j])
            print("对应作者是：")
            print(i['author'][j])
            print("----------------------")
        return i
