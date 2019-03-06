# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast' #爬虫名字
    allowed_domains = ['itcast.cn'] #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  #最开始请求的url地址

    def parse(self, response): # TODO 这个函数名不能改，规定就这个名字parse
        # TODO 处理start_urls地址对应的响应，
        #
        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()")
        # print(ret1) # ret1 是一个列表，里面是对象

        # ret1 = response.xpath("//div[@class='tea_con']//h3/text()").extract()
        # print(ret1) # ret1 是一个列表，里面是对象 extract()可以提取文字

        # 分组
        li_list = response.xpath("//div[@class='tea_con']//li")
        for li in li_list:
            item = {}
            # 这里的xpath写错了，extract_first() 获取不到数据返回None，有数据返第一个
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)

            # 把item变成一个生成器，减少内存占用
            # TODO ？？在这里yield后面必需是Request,BaseItem,dict or None,不能是列表
            yield item #框架内部直接把item直接传给pipelines.py
