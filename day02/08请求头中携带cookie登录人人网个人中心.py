import requests
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Safari/537.36",
    "Cookie": "anonymid=jkchhdtc64ku6k; depovince=GW; _r01_=1; JSESSIONID=abc-_seH78rGq9t_7A6tw; ick_login=bec756b5-7b31-4f64-a9c4-9e1bead87b1d; t=6c9398805d993f6b039584408f3d675f1; societyguester=6c9398805d993f6b039584408f3d675f1; id=967245901; xnsid=58f5b58; jebecookies=33f89001-10fd-48e5-b3f9-27c152a43786|||||; jebe_key=94b111dd-51dd-4312-812b-80b00b227f82%7Cf8feac1367ea7190d33c4e06f4cb5fc5%7C1533210137201%7C1%7C1533210146052; wp_fold=0; __utma=151146938.870996965.1533212060.1533212060.1533212060.1; __utmc=151146938; __utmz=151146938.1533212060.1.1.utmcsr=renren.com|utmccn=(referral)|utmcmd=referral|utmcct=/967245901/profile; __utmb=151146938.1.10.1533212060"
}

r= requests.get("http://www.renren.com/967245901/profile",headers=headers)

with open("08请求头中携带cookie登录人人网个人中心.html","w",encoding="utf-8") as f:
    f.write(r.content.decode())