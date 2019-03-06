# coding=utf-8

import re
import requests


def dowmloadPic(html, keyword):
    pic_url = re.findall('"objURL":"(.*?)",', html, re.S)
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    for each in pic_url:
        print('正在下载第' + str(i) + '张图片，图片地址:' + str(each))
        try:
            pic = requests.get(each, timeout=10)
        except requests.exceptions.ConnectionError:
            print('【错误】当前图片无法下载')
            continue

        with open("./mm/{}.jpg".format(str(i)), "wb") as f:
            f.write(pic.content)
        # dir = '../images/' + keyword + '_' + str(i) + '.jpg'
        # fp = open(dir, 'wb')
        # fp.write(pic.content)
        # fp.close()
        i += 1
# Query  String Parameters 随机参数

if __name__ == '__main__':
    word = input("Input key word: ")
    # https://m.baidu.com/sf/vsearch/image/search/wisejsonala?tn=wisejsonala&ie=utf8&cur=result&fromsf=1&word=%E5%90%89%E5%A8%83%E5%A8%83&pn=30&rn=30&gsm=1e
    url = 'http://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word=' + word + '&ct=201326592&v=flip'
    result = requests.get(url)
    print(result.text) #result提取的是一个html页面
    dowmloadPic(result.text, word)

# http://pic.xiudodo.com/figure/00/00/33/16/73/1655bda6abbcd26.jpg
# http:\/\/img5.duitang.com\/uploads\/item\/201412\/23\/20141223134318_jUumA.thumb.700_0.jpeg