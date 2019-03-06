import requests
from lxml import etree
import json


class TiebaSpider:
    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36"}
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+self.tieba_name+"&pn=20"
        self.part_url ="http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/" #用于url前缀拼凑
    def send_request(self,next_page_url):
        """2. 发送请求获取响应"""
        # print("-"*100)
        # print(next_page_url)
        # print(requests.get(url=next_page_url,headers=self.headers))

        response_obj = requests.get(url=next_page_url,headers=self.headers)  #返回response对象
        response_bytes_str = response_obj.content  #取出它的内容content，是二进制数据
        return response_bytes_str

    def filter_data(self,response_html_bytes):
        """3. 提取当前页想要的数据，并提取下一页的url"""
        html_obj = etree.HTML(response_html_bytes) #返回一个html对象
        # print(html)  <Element html at 0x3535108>

        #提取当前页想要的数据，要分块div获取，不然会乱
        div_list = html_obj.xpath('//div[contains(@class,"i")]')
        content_div_list = []

        for div_item in div_list:
            div_data_dict = {}
            div_data_dict["title"] = div_item.xpath('./a/text()')[0] if len(div_item.xpath('./a/text()')) else None
            div_data_dict["href"] = self.part_url+ div_item.xpath('./a/@href')[0] if len(div_item.xpath('./a/@href')) else None
            div_data_dict["img_list"] = self.get_img_list(div_data_dict["href"],[])
            div_data_dict["img_list"] = [requests.utils.unquote(i).split("src=")[-1] for i in div_data_dict["img_list"]]

            content_div_list.append(div_data_dict)


        #提取下一页的url
        # next_page_url = html_obj.xpath('//body/form[@action="m"]//a[text()="下一页"]/@href')
        next_page_url =self.part_url + html_obj.xpath("//a[text()='下一页']/@href")[0] if len(html_obj.xpath("//a[text()='下一页']/@href")) else None
        print(next_page_url)  #['m?kw=%E5%81%9A%E5%A4%B4%E5%8F%91&lp=5011&lm=&pn=40']

        return content_div_list, next_page_url


    def get_img_list(self,detail_url,total_img_list): #获取帖子中的所有的图片

        # 3.2请求列表的url地址，获取详情页的第一页
        detail_html_str = self.send_request(detail_url)
        detail_html_obj = etree.HTML(detail_html_str)
        # 3.3 提取详情页的第一页图片，提取下一页的地址
        img_list = detail_html_obj.xpath("//img[@class='BDE_Image']/@src")
        total_img_list.extend(img_list)
        # 3.4 请求详情页下一页的地址，进入循环3.2-3.4

        detail_next_page_url = detail_html_obj.xpath("//a[text()='下一页']/@href")
        if len(detail_next_page_url)>0:  #递归的出口条件，没有下一页的时候，此处也可以用循环
            detail_next_page_url = self.part_url + detail_next_page_url[0]
            return self.get_img_list(detail_next_page_url,total_img_list)
        return total_img_list

    def save_data(self,content_div_list):
        """4. 保存数据"""
        file_path = self.tieba_name + '.txt'
        with open(file_path,"a",encoding="utf-8") as f:
            for content in content_div_list:
                # f.write(str(content))
                # f.write(),必需接收字符串，json也是字符串，是漂亮的字符串
                f.write(json.dumps(content,ensure_ascii=False,indent=4))
                f.write("\n")
        print("保存成功")



    def run(self):
        """实现主要逻辑"""
        next_page_url = self.start_url
        while next_page_url is not None:
            # 1. start_url，在初始化函数里
            # 2. 发送请求获取响应
            response_html_bytes = self.send_request(next_page_url)

            # print(response_html)
            # 3. 提取当前页想要的数据，并提取下一页的url
            get_data,next_page_url = self.filter_data(response_html_bytes)
            #     3.1 提取列表页的url地址和标题
            #     3.2 请求列表的url地址，获取详情页的第一页
            #     3.3 提取详情页的第一页图片，提取下一页的地址
            #     3.4 请求详情页下一页的地址，进入循环3.2-3.4
            # 4. 保存数据
            self.save_data(get_data)
            # 5. 请求下一页的url，进入循环2-5

if __name__ == "__main__":
    spider_obj = TiebaSpider("做头发")
    spider_obj.run()
