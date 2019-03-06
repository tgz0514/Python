# -*- coding: utf-8 -*-
import scrapy
import json
import urllib
from copy import deepcopy


class JdSpider(scrapy.Spider):
    name = 'jd'
    allowed_domains = ['jd.com','p.3.cn']
    start_urls = ['https://book.jd.com/booksort.html']

    def parse(self, response):
        dt_list = response.xpath("//div[@class='mc']/dl/dt") #获取大分类列表，如小说，文学，传记
        for dt in dt_list:
            item = {}
            item["b_cate"] = dt.xpath("./a/text()").extract_first()
            # following-sibling::div[1] 表示当前节点的兄弟节点中的 第 1 个 div标签
            em_list = dt.xpath("./following-sibling::dd[1]/em") #小分类列表
            for em in em_list:
                item["s_href"] = em.xpath("./a/@href").extract_first() #小分类url
                item["s_cate"] = em.xpath("./a/text()").extract_first() # 小分类名称
                if item["s_href"] is not None:
                    item["s_href"] = "https:" + item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback=self.parse_book_list,
                        meta={"item":deepcopy(item)}  # TODO 这里要deepcopy
                    )

    def parse_book_list(self,response): #解析小分类列表页
        item = response.meta["item"]
        #获取小分类下所有图书的li标签列表，每一本书都是一个单独的li
        li_list = response.xpath("//div[@id='plist']/ul/li")
        for li in li_list:
            item["book_img"] = li.xpath(".//div[@class='p-img']//img/@src").extract_first()
            if item["book_img"] is None:
                item["book_img"] = li.xpath(".//div[@class='p-img']//img/@data-lazy-img").extract_first()
            #strip() 方法用于移除字符串头尾指定的字符,不传参数默认删除头、尾空白字符
            item["book_img"]="https:"+item["book_img"] if item["book_img"] is not None else None

            item["book_name"] = li.xpath(".//div[@class='p-name']/a/em/text()").extract_first().strip()
            item["book_author"] = li.xpath(".//span[@class='author_type_1']/a/text()").extract() #作者可能有多个，所以用extract
            item["book_press"] = li.xpath(".//span[@class='p-bi-store']/a/@title").extract_first()
            item["book_publish_date"] = li.xpath(".//span[@class='p-bi-date']/text()").extract_first().strip()
            item["book_sku"] = li.xpath("./div/@data-sku").extract_first() #获取每本图书的sku---图书的唯一编号
            # 通过获取的编号，构造请求获取图书价格
            yield scrapy.Request(
                # 这里情求的域名和前面的不一样，要添加到allowed_domains允许域名列表中
                "https://p.3.cn/prices/mgets?skuIds=J_{}".format(item["book_sku"]),
                callback=self.parse_book_price,
                meta = {"item":deepcopy(item)}  # TODO 这里要deepcopy
            )

        # 列表页翻页
        next_url = response.xpath("//a[@class='pn-next']/@href").extract_first()
        if next_url is not None:
            # TODO 看不懂
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse_book_list, #回调函数是自己
                meta={"item":item}
            )


    def parse_book_price(self,response):
        item = response.meta["item"]
        #把响应体里的json转化为python列表，取第一个元素（本质是一个字典）的op键对应的值（图书价格），
        item["book_price"] = json.loads(response.body.decode())[0]["op"]
        print(item)


