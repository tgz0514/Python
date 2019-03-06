import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"}
url="https://www.baidu.com/s?&wd={}".format("python")
r = requests.get(url=url,headers=headers)
print(r.status_code)
print(r.request.url)