import re
import requests
import json
def downloadPic(html,keyword):
    # https: // m.baidu.com / sf / vsearch / image / search / wisejsonala?tn = wisejsonala & ie = utf8 & cur = result & fromsf = 1 & word = % E5 % A3 % 81 % E7 % BA % B8 & pn = 30 & rn = 30 & gsm = 1
    # e
    #"http:\/\/imgsrc.baidu.com\/imgad\/pic\/item\/e7cd7b899e510fb3162681b5d333c895d1430cd0.jpg"
    pic_url = re.findall(r'"obj_url":"(.*?)"',html,re.S)
    #['http:\\/\\/www.cssxt.com\\/uploadfile\\/2017\\/1208\\/20171208110834538.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/f31fbe096b63f6242f29f42b8c44ebf81a4ca3a6.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/b64543a98226cffc9210e0acb3014a90f603eaf2.jpg', 'http:\\/\\/imgsrc.baidu.com\\/image\\/c0%3Dshijue1%2C0%2C0%2C294%2C40\\/sign=9f9dec00ba51f819e5280b09b2dd2098\\/8718367adab44aed88fcd4cfb91c8701a18bfb6f.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/b17eca8065380cd7761deff4ab44ad34598281ac.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/8694a4c27d1ed21b559175c0a76eddc451da3fbe.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/38dbb6fd5266d0162fb4060c9d2bd40735fa3560.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/d009b3de9c82d1584bde7b968a0a19d8bc3e42bc.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/962bd40735fae6cd3ce40c9705b30f2443a70ff7.jpg', 'http:\\/\\/imgs.aixifan.com\\/content\\/2016_06_07\\/1465274192.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/2e2eb9389b504fc2bb7d8821efdde71190ef6df7.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/cefc1e178a82b9017e313214788da9773912ef7d.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/dc54564e9258d1090a197eaedb58ccbf6c814d30.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/d1160924ab18972b1c8f38e3edcd7b899e510a65.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/203fb80e7bec54e74d30d43cb3389b504fc26a30.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/d6ca7bcb0a46f21fc450aba6fc246b600d33aedb.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/d0c8a786c9177f3ef549e9c47acf3bc79e3d56fd.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/0eb30f2442a7d93393d35554a74bd11373f00199.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/faedab64034f78f084e7d6d773310a55b3191c21.jpg', 'http:\\/\\/pic122.nipic.com\\/file\\/20170216\\/24421947_173534660000_2.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/bd3eb13533fa828b2ff2b5c4f71f4134960a5ac7.jpg', 'http:\\/\\/image5.tuku.cn\\/pic\\/wallpaper\\/fengjing\\/langmanshatansheyingbizhi\\/020.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/b17eca8065380cd7876bde19ab44ad34588281c8.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/562c11dfa9ec8a1377806ee9fd03918fa0ecc024.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/42a98226cffc1e17b1c805c44090f603728de9d4.jpg', 'http:\\/\\/imgsrc.baidu.com\\/image\\/c0%3Dshijue1%2C0%2C0%2C294%2C40\\/sign=7f60560430292df583cea456d4583615\\/e1fe9925bc315c60df26f8c487b1cb134954776e.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/f2deb48f8c5494eeec90573326f5e0fe99257e6d.jpg', 'http:\\/\\/www.wallcoo.com\\/other\\/201305_May_calendar_wallpapers\\/wallpapers\\/1440x900\\/may-13-puppet_show-calendar.jpg', 'http:\\/\\/imgsrc.baidu.com\\/imgad\\/pic\\/item\\/7aec54e736d12f2e17db519645c2d5628435686e.jpg', 'http:\\/\\/www.zcool.com.cn\\/community\\/037d6f158b977b4a801219c7712bc5e.jpg']
    # pic_url=",".split(pic_url)

    print(pic_url)
    print(len(pic_url))
    i = 1
    print('找到关键词:' + keyword + '的图片，现在开始下载图片...')
    headers = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36"}
# Accept-Language: zh-CN,zh;q=0.9
#
# Connection: keep-alive
# Host: www.hinews.cn
#
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3423.2 Mobile Safari/537.36"
#

# "Referer":"https://m.baidu.com/sf/vsearch?pd=image_content&word=%E8%B6%85%E9%AB%98%E6%B8%85%E5%A3%81%E7%BA%B8&tn=vsearch&atn=page"}
    for url in pic_url:

        # b = re.findall(r"[^\\]*", url)
        # url = "".join(b)
        url = re.sub(r'\\','',url)

        print('正在下载第' + str(i) + '张图片，图片地址:' + str(url))
        try:
            pic = requests.get(url=url,timeout=10)
        except requests.RequestException:
            print('【错误】当前图片无法下载')
            continue

        with open("./mm/{}.jpg".format(str(i)),'wb') as f:
            f.write(pic.content)

        i += 1

if __name__ == "__main__":
    word = input("输入想要搜索的图片名称：")

    url = "https://m.baidu.com/sf/vsearch/image/search/wisejsonala?tn=wisejsonala&ie=utf8&cur=result&fromsf=1&word={}&pn=30&rn=4&gsm=1e".format(word)
    # ret = requests.get(url=url).content.decode()
    # json.loads(response.content.decode())
    ret = requests.get(url=url).content.decode()
    print(type(ret))
    # ret = json.loads(ret)

    print(ret) #ret提取的是一个数据包
    downloadPic(ret,word)