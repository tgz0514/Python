# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# pipelines这个文件帮我们处理数据(管道，保存数据)
class MyspiderPipeline(object):
    # TODO 这个函数名不能改，规定就这个名字process_item
    def process_item(self, item, spider):
        item["hello"] = "world"
        # print(item)
        return item #这里必需有return,作用是让后面的pipelines能接收到值，不然后面都是None

class MyspiderPipeline1(object):
    def process_item(self, item, spider):

        print(item)
        return item
