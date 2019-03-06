import requests
import json
import sys

class BaiduFanyi:
    def __init__(self,trans_str):
        self.trans_str = trans_str #这是要翻译的字符串
        self.lang_detect_url = "https://fanyi.baidu.com/langdetect" # 判断翻译语种的url
        # self.trans_url = "https://fanyi.baidu.com/v2transapi"
        # self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"}
        # 手机版
        self.trans_url = "http://fanyi.baidu.com/basetrans"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    # 发送post请求，获取响应
    def parse_url(self,url,data):
        response = requests.post(url,data=data,headers=self.headers)
        # TODO response.content.decode()到底是普通字符串，还是json字符串
        return json.loads(response.content.decode())  #把json字符串转化为python对象，可能是列表，也可能是字典，这取决于原json数据

    # 提取翻译结果
    def get_ret(self,dict_response):
        ret = dict_response["trans"][0]["dst"]
        print("result is :", ret)

    def run(self): #实现主要逻辑

        #1.获取语言类型
            #1.1 准备post的url地址，post_data
        lang_detect_data = {"query":self.trans_str} # query: 开心  ,要翻译的单词，模仿成要发送给百度翻译的字典data

            # 1.2 发送post请求，获取响应
        lang = self.parse_url(self.lang_detect_url,lang_detect_data)
            # 1.3 提取语言类型
        lang = lang["lan"] #{error: 0, msg: "success", lan: "zh"}

        # 2.准备post的数据
        trans_data = {"query": self.trans_str,"from": "zh","to": "en"} if lang == "zh" \
            else {"query": self.trans_str,"from": "en","to": "zh"}
        # 3.发送请求，获取响应
        dict_response = self.parse_url(self.trans_url,trans_data)
        # 4.提取翻译的结果
        self.get_ret(dict_response)


if __name__ == '__main__':
    trans_str = sys.argv[1] #python 01网页版百度翻译.py 今天风很大啊
    baidu_fanyi = BaiduFanyi(trans_str)
    baidu_fanyi.run()