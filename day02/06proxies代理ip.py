import requests

proxies = {"http":"http://117.158.174.164:8060"}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"
}
r = requests.get("http://www.baidu.com",proxies=proxies,headers=headers)
print(r.status_code)