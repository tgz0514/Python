import requests
import json
class DoubanSpider:
    def __init__(self):
        self.url_temp_list = [
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_american_hot/items?start={}&count=18&loc_id=108288",
                "country": "US"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_english_hot/items?start={}&count=18&loc_id=108288",
                "country": "UK"
            },
            {
                "url_temp": "https://m.douban.com/rexxar/api/v2/subject_collection/filter_tv_domestic_hot/items?start={}&count=18&loc_id=108288",
                "country": "CN"
            }
        ]
        self.headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Mobile Safari/537.36",
                        "Referer":"https://m.douban.com/movie/nowintheater?loc_id=108288"}

    # TODO 2. 发送请求，获取响应
    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content.decode()

    # TODO 3. 提取数据
    def get_content_list(self,json_str):
        dict_ret = json.loads(json_str)
        # 返回的dict_ret格式是字典：  "subject_collection_items":[18tiao数据]
        print(dict_ret)
        content_list = dict_ret["subject_collection_items"]
        total = dict_ret["total"] #共多少条数据
        return content_list, total

    # TODO 4. 保存数据
    def save_content_list(self,content_list,country):
        with open("豆瓣.txt","a",encoding="utf-8") as f:
            #先打开文件，再遍历不用反复打开关闭，节省时间
            for content in content_list:
                # 给coutent额外添加一个国家字段
                content["country"] = country
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n") #写入换行符，进行换行

        print("保存成功")
    # TODO 实现主要逻辑
    def run(self):
        for url_temp in self.url_temp_list:
            num = 0
            # 方法一：用total判断是否需要停止循环
            # total = 100 #假设有第一页
            # while num<total + 18:
            # 方法二：
            while True:
                # TODO 1. 起始url
                url = url_temp["url_temp"].format(num)
                # TODO 2. 发送请求，获取响应
                json_str = self.parse_url(url)
                # TODO 3. 提取数据
                content_list,total = self.get_content_list(json_str)
                # TODO 4. 保存数据
                self.save_content_list(content_list,url_temp["country"])
                #默认每页加载18条数据，当有一页不足18条是，说明没有了，break停止循环
                if len(content_list) < 18:
                    break
                # TODO 5. 构造下一页的url地址，进入循环
                num += 18

if __name__ == "__main__":
    douban = DoubanSpider()
    douban.run()

