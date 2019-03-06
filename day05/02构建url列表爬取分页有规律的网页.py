import requests
from lxml import etree
import json

"""
爬取糗百，因为糗百网页分页很有规律，所以我们可以构建url列表爬取

"""
class QiubaiSpdier:
    def __init__(self):
        #temp临时。构建临时url
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}

    def get_url_list(self): #构造url列表
        return [self.url_temp.format(i) for i in range(1,14)]

    def parse_url(self,url): #发送请求
        print(url)
        response = requests.get(url=url,headers=self.headers)
        return response.content
    def get_content_list(self,html_str): #提取数据,使用xpath
        html = etree.HTML(html_str) #返回一个对象，只有html对象才能使用xpath
        div_list = html.xpath("//div[@id='content-left']/div")
        content_list = []
        for div in div_list:
            item = {}
            item["content"] = div.xpath(".//div[@class='content']/span/text()")
            # replace() 方法把字符串中的 old（旧字符串） 替换成 new(新字符串
            item["content"] = [i.replace("\n","") for i in item["content"]]
            item["author_gender"] = div.xpath(".//div[contains(@class,'articleGender')]/@class") #获取class的属性值
            item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon","") if len(item["author_gender"]) else None
            item["auhtor_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            item["auhtor_age"] = item["auhtor_age"][0] if len(item["auhtor_age"]) else None
            item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
            item["content_img"] = "https:"+item["content_img"][0] if len(item["content_img"])>0 else None
            item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            item["author_img"] = "https:"+item["author_img"][0] if len(item["author_img"])>0 else None
            item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None

            content_list.append(item)
            print(item)
        return content_list
    def save_content_list(self,content_list): #保存数据
        with open("./02糗事百科.txt","w",encoding="utf-8") as f:
            for i in content_list:
                f.write(json.dumps(i,ensure_ascii=False,indent=4))
                f.write("\n")

    def run(self): #启动方法，实现主要逻辑
        # 1. 构造url_list
        url_list = self.get_url_list()
        # 2. 遍历url_list,发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)
            # 3. 提取数据
            content_list = self.get_content_list(html_str)
            # 4. 保存数据
            self.save_content_list(content_list)
if __name__ == "__main__":
   qiubai = QiubaiSpdier()
   qiubai.run()