import requests
import os


def getPages(keyword, pages):
    params = []
    for i in range(30, 30 * pages + 30, 30):
        params.append({
            'tn': 'resultjson_com',
            'ipn': 'rj',
            'ct': 201326592,
            'is': '',
            'fp': 'result',
            'queryWord': keyword,
            'cl': 2,
            'lm': -1,
            'ie': 'utf-8',
            'oe': 'utf-8',
            'adpicid': '',
            'st': -1,
            'z': '',
            'ic': 0,
            'word': keyword,
            's': '',
            'se': '',
            'tab': '',
            'width': '',
            'height': '',
            'face': 0,
            'istype': 2,
            'qc': '',
            'nc': 1,
            'fr': '',
            'pn': i,
            'rn': 30,
            'gsm': '1e',
            '1488942260214': ''
        })
    url = 'https://image.baidu.com/search/acjson'
    urls = []
    for i in params:
        # TODO requests.get(url, params=i).json()这是什么写法
        urls.append(requests.get(url, params=i).json().get('data'))

        print(requests.get(url, params=i).json()) # TODO
        print(requests.get(url,params=i).json().get('data'))
    return urls


# dataList = urls
def getImg(dataList, localPath):
    print("*"*100)
    print(dataList)
    if not os.path.exists(localPath):
        os.mkdir(localPath)

    try:
        x = 0
        for list in dataList:
            for i in list:
                if i.get('thumbURL') != None:
                    print('正在下载：%s' % i.get('thumbURL'))
                    ir = requests.get(i.get('thumbURL'))
                    open(localPath + '%d.jpg' % x, 'wb').write(ir.content)
                    x += 1
        print('图片下载完成')
    except Exception:
        print("图片下载失败")


if __name__ == '__main__':
    dataList = getPages('吉娃娃', 3)
    getImg(dataList, './image/')
