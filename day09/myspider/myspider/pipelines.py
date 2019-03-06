# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.getLogger(__name__)


class MyspiderPipeline(object):
    def process_item(self, item, spider): #接收爬虫传过来的item,spider是spiders.py文件下的ItcastSpider这个类
        if spider.name == "itcast": #这两个if的作用一样，都是判断是那个爬虫
        # if item["come_from"] == "itcast":
            logger.warning("-"*30)
        return item #这里必需有return,作用是让后面的pipelines能接收到值，不然后面都是None

class MyspiderPipeline2(object):
    def process_item(self, item, spider): #接收爬虫传过来的item,spider是spiders.py文件下的ItcastSpider这个类
        if spider.name == "itcast1": #这两个if的作用一样，都是判断是那个爬虫
        # if item["come_from"] == "jd":
            pass
        return item #这里必需有return,作用是让后面的pipelines能接收到值，不然后面都是None
