# -*- coding: utf-8 -*-
import scrapy
import logging

# 实例化一个logger
logger = logging.getLogger(__name__)

class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫的名字
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response): #这个函数名不能变，提取数据，接收下载中间件传过来的response
        # 增加字段，让pipeline知道是那个spider
        for i in range(10):
            item = {}
            item["come_from"] = "itcast"
            # logging.warning(item) #把log日志输出出来warning等级
            logger.warning(item) #把log日志输出出来warning等级

            # 把item变成一个生成器，减少内存占用
            # TODO ？？在这里yield后面必需是Request,BaseItem,dict or None,不能是列表
            yield item  # 框架内部直接把item直接传给pipelines.py

            # yield 后面跟 BaseItem，dict给pipelines.py处理
            # yield 后跟 Request 给