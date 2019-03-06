import requests


class BaiduTranslate:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"
        }
        self.post_url = "http://fanyi.baidu.com/v2transapi"

        self.data = {
            "from": "en",
            "to": "zh",
            "query": "python",
            "transtype": "translang",
            "simple_means_flag": "3",
            "sign": "477811.239938",
            "token": "69d72ea6eb2dbb7ebb0b59892101d49b"
        }
    def run(self):
        ret = requests.post(self.post_url,data=self.data,headers=self.headers)
        print(ret.content.decode())

result = BaiduTranslate()
result.run()