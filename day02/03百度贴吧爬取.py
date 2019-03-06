# coding=utf-8
import requests


class TibaSpider:
    def __init__(self, tieba_name, page_num):
        # 1.关键词：tieba_name
        self.tieba_name = tieba_name
        self.page_num = page_num
        # 2.请求的url：url_temp
        self.url_temp = "http://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        # 3.请求头，用于模拟浏览器请求，防止服务器判定是爬虫
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"
        }

    def get_url_list(self):
        """
        构造url列表
        :return:
        """
        # 方法一：分步写
        # url_list = []
        # for i in range(10):
        #     url_list.append(self.url_temp.format(i*50))
        # return url_list

        # 方法二：用列表推导式
        return [self.url_temp.format(i * 50) for i in range(self.page_num)]

    def parse_url(self, url):
        """发送请求，获取响应"""
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def save_html(self, html_str, page_num):
        """保存html字符串"""
        file_path = "{}-第{}页.html".format(self.tieba_name, page_num)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(html_str)

    def run(self):
        """实现主要逻辑"""
        # 1.构造url列表
        url_list = self.get_url_list()
        # 2.遍历列表，过去响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3.保存响应内容
            page_num = url_list.index(url) + 1  # 页码数
            self.save_html(html_str, page_num)


if __name__ == '__main__':
    tiba_spider = TibaSpider("python", 10)
    tiba_spider.run()
