import requests
import re
import os


class Mei:

    def __init__(self):
        self.url = "http://www.27270.com/ent/meinvtupian/"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Safari/537.36"}
        self.image_list = []
        # 创建一个保存图片的文件夹
        if(not os.path.exists("./mm")):
            os.mkdir("./mm")


    def get_image_list(self):
        # 1- 获得网页字符串
        response = requests.get(self.url,headers = self.headers)
        html_str = response.content.decode("gbk")
        print(html_str)
        # 2- 从网页中，使用正则式，将需要的数据 提取出来
        ret = re.findall(r"<li>.*?class=\"MMPic\".*?</li>",html_str,re.S)
        for item in ret:
            print(item)
            image_url = re.search(r"<img src=\"(http://.*?\.jpg)\"",item,re.S).group(1)
            print("image_url:"+image_url)
            title = re.search(r"title=\"(.*?)\"",item,re.S).group(1)
            print("title:"+title)
            print('+'*40)
            image_dict = {"title":title,"url":image_url}
            self.image_list.append(image_dict)

    def run(self):
        # 1- 获得所有的标题和图片的url
        self.get_image_list()
        # 2- 下载所有的图片
        for item in self.image_list:
            title  = item["title"]
            url = item["url"]
            print("下载: "+url)
            # 下载图片
            image_resp = requests.get(url,headers=self.headers)
            with open("./mm/{}.jpg".format(title), "wb") as f:
                f.write(image_resp.content)



if __name__ == '__main__':
    mei = Mei()
    mei.run()