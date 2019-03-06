import requests
from lxml import etree
import json
from queue import Queue
import threading

"""
爬取糗百，因为糗百网页分页很有规律，所以我们可以构建url列表爬取

"""
class QiubaiSpdier:
    def __init__(self):
        #temp临时。构建临时url
        self.url_temp = "https://www.qiushibaike.com/8hr/page/{}/"
        self.headers = {"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36"}
        self.url_queue = Queue() #创建一个url池
        self.html_queue = Queue() #创建一个服务器返回的数据的html池
        self.content_queue = Queue() #创建一个存放提取数的数据池
    def get_url_list(self): #构造线程池

        # 向线程池添加url
        for i in range(1,14):
            self.url_queue.put(self.url_temp.format(i))

    def parse_url(self): #发送请求,获取响应
        while True:
            url = self.url_queue.get() #从线程池取出一个线程
            print(url)
            response = requests.get(url=url,headers=self.headers)
            # return response.content
            #把获取的数据放入html池u
            self.html_queue.put(response.content.decode())
            self.url_queue.task_done() #每task_done一次 就从队列里删掉一个元素

    def get_content_list(self): #提取数据,使用xpath
        while True:
            html_str = self.html_queue.get()
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
                # print(item)
            self.content_queue.put(content_list) #把提取的数据放入数据池中
            self.html_queue.task_done() #每task_done一次 就从队列里删掉一个元素

    def save_content_list(self): #保存数据

        with open("./02糗事百科.txt","w",encoding="utf-8") as f:
            while True:
                content_list = self.content_queue.get() #从数据池中获取一个线程的结果
                for i in content_list:
                    f.write(json.dumps(i,ensure_ascii=False,indent=4))
                    f.write("\n")

                self.content_queue.task_done() #每task_done一次 就从队列里删掉一个元素

    def run(self): #启动方法，实现主要逻辑
        thread_list = []
        # 1. 构造url_list
        t_url = threading.Thread(target=self.get_url_list)
        thread_list.append(t_url)
        # 2. 发送请求，获取响应
        for i in range(20): #给三个线程做发送请求
            t_parse = threading.Thread(target=self.parse_url)
            thread_list.append(t_parse)
        # 3. 提取数据
        for i in range(3): #给两个线程做提取数据
            t_html = threading.Thread(target=self.get_content_list)
            thread_list.append(t_html)
        # 4. 保存数据
        t_save = threading.Thread(target=self.save_content_list)
        thread_list.append(t_save)

        for t in thread_list:
             # TODO setDaemon可以让while Ture 在主线程结束的时候停止
            t.setDaemon(True)  # 把子线程设置为守护线程，该线程不重要,主线程结束，子线程结束
            t.start() #启动线程
        for q in [self.url_queue,self.html_queue,self.content_queue]:
            q.join() #让主线程等待阻塞，等待所有队列的任务完成之后再完成
        print("主线程结束")

if __name__ == "__main__":
   qiubai = QiubaiSpdier()
   qiubai.run()