import requests
import json

class BaiduTranslate:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36"
        }
        self.post_url = "http://fanyi.baidu.com/basetrans"

        self.data = {
            "from": "zh",
            "to": "en",
            "query": "人生苦短，我用Python",
         }
    def run(self):

        ret = requests.post(self.post_url,data=self.data,headers=self.headers)
        # print(type(ret))#返回的ret是一个对象<class 'requests.models.Response'>
        # con = ret.content.decode()
        # print(con)
        cont = ret.content.decode()
        print(cont)
        dict_con = json.loads(cont) #把json字符串转化为字典
        # print(dict_con)
        result = dict_con["trans"][0]["dst"]
        print(result)
        print(type(result))
        return result

    # def __str__(self):
    #     return "result is :%s" % result

result = BaiduTranslate()
result.run()
print("result is :",result.run())