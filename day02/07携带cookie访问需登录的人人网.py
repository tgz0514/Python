import requests
url = "http://www.renren.com/PLogin.do"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36"
}
post_data = {"email":"mr_mao_hacker@163.com", "password":"alarmchime"}

#创建session对象
session=requests.session()
#使用session发送post请求，cookie保存在其中
session.post(url=url,data=post_data, headers = headers)
r = session.get('http://www.renren.com/327550029/profile',headers = headers)

#保存页面
with open("07携带cookie访问需登录的人人网.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())