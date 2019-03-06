import json
import requests
from day03.parse_url import parse_url
from pprint import pprint  #把打印的内容格式化一下输出


# url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=18&loc_id=108288"
url = "https://m.douban.com/rexxar/api/v2/subject_collection/movie_showing/items?start=0&count=8&loc_id=108288"
# pprint(url)
html_str = parse_url(url)  #返回的是一个json字符串

# json.loads把json字符串转化为python类型
ret1 = json.loads(html_str)  #<class 'dict'>
# pprint(ret1)
# print(type(ret1))

#json.dump能够把python类型放入类文件对象中
with open("豆瓣.json","w",encoding="utf-8") as f:
    f.write(json.dumps(ret1,ensure_ascii=False,indent=4))

# 经过json.dumps(ret1,ensure_ascii=False,indent=4)的字符串，
# 一样可以被json.loads()方法变回原来的python对象
with open("豆瓣.json","r",encoding="utf-8") as f:
    ret2 = f.read()
    ret3 = json.loads(ret2)
    print(ret3)
    print(type(ret3))