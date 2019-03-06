# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html


import random
# 自定义一个随机UserAgent中间件
class RandomUserAgentMiddleware:
    def process_request(self,request,spider):

        # 在setting.py配置文件里有自定义的UserAgent列表，通过spider可以获取setting.py的内容
        #从列表中随机获取一个User-Agent
        UserAgent=random.choice(spider.settings.get("USER_AGENTS_LIST"))
        request.headers["User-Agent"] = UserAgent #随机获取的User-Agent假如请求头

#自定义一个类，检查User-Agent是否被添加
class CheckUserAgent:
    def process_response(self,request,response,spider):
        # print(dir(response.request)) #查看response有哪些方法
        print(request.headers["User-Agent"]) #检查User-Agent是否被添加

        return response #必需有return

        """
        :return response 表示通过引擎交给spider
        :return request 表示通过引擎交给调度器
        """
