# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CfSpider(CrawlSpider):
    name = 'cf'
    allowed_domains = ['circ.gov.cn']
    start_urls = ['http://bxjg.circ.gov.cn/web/site0/tab5240/']

    #定义提取url地址规则
    rules = (
        #实例化一个Rule。参数LinkExtractor：链接提取器，通过正则提取url
        #callback: 提取出来的url地址的response会交给callback指定的函数提取想要的数据
        #follow 当前url地址的响应是否重新经过rules/LinkExtractor来提取url地址
        # 正则提取首页每条信息详情页的url =  /web/site0/tab5240/info4102978.htm
        # url不完整，CraelSpider会在请求的时候自动补充完整
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/info\d+\.htm'), callback='parse_item'), #筛选详情页url
        # TODO 提取翻页url,1,2,3,4...
        # TODO 为何不用指定url给谁发起请求？？？
        Rule(LinkExtractor(allow=r'/web/site0/tab5240/module14430/page\d+\.htm'),follow=True)  #筛选翻页url
    )

    # parse函数有特殊功能，不能定义
    def parse_item(self, response):
        """
        i = {}
        i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        i['name'] = response.xpath('//div[@id="name"]').extract()
        i['description'] = response.xpath('//div[@id="description"]').extract()
        :param response: 
        :return: 
        """"""
       """
        item = {}
        item["title"] = re.findall("<!--TitleStart-->(.*?)<!--TitleEnd-->",response.body.decode())[0]
        item["publish_date"] = re.findall("发布时间：(20\d{2}-\d{2}-\d{2})",response.body.decode())[0]
        print(item)

        # 假如详情页有数据要提取，在列表页也有数据要提取，我们可以构造请求
    #     yield scrapy.Request(
    #         url="...",
    #         callback=self.parse_detail
    #         meta = {"item":item}
    #     )
    #
    # def parse_detail(self,response):
    #     item = response.meta["item"]  # 获取传过来的meta数据
"""yield 后跟一个item 和跟一个函数调用不一样"""
        # 下面这几步是给item添加数据，最后yield一个完整的item字典数据
        # item["content"] = response.xpath("//div[@class='c1 text14_2']//text()").extract()
        # item["content_img"] = response.xpath("//div[@class='c1 text14_2']//img/@src").extract()
        # item["content_img"] = ["http://wz.sun0769.com" + i for i in item["content_img"]]
        # # print(item)
        # yield item
