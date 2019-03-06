from lxml import etree

text = ''' <div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </ul> </div> '''

html = etree.HTML(text) #利用etree.HTML，将字符串转化为Element对象
print(html)  #<Element html at 0x11e3688>

# etree.tostring()查看element对象包含的字符串
# print(etree.tostring(html).decode())
"""
etree.tostring()查看element对象包含的字符串
print(etree.tostring(html).decode()) 输出的内容如下：


<html><body><div> <ul> 
        <li class="item-1"><a>first item</a></li> 
        <li class="item-1"><a href="link2.html">second item</a></li> 
        <li class="item-inactive"><a href="link3.html">third item</a></li> 
        <li class="item-1"><a href="link4.html">fourth item</a></li> 
        <li class="item-0"><a href="link5.html">fifth item</a>  
        </li></ul> </div> </body></html>
"""


#获取class为item-1 下的 herf
ret1 = html.xpath("//li[@class='item-1']/a/@href")
print(ret1) #['link2.html', 'link4.html']

#获取class为item-1 li下a的文本
ret2=html.xpath("//li[@class='item-1']/a/text()")
print(ret2) #['first item', 'second item', 'fourth item']

# 每个li是一条新闻，把url和文本组成字典
for href in ret1:
    item = {}
    item["href"] = href
    item["title"] = ret2[ret1.index(href)]
    print(item)

print("*"*70)




# TODO 分组，根据li标签进行分组，对每一组继续写xpath

#利用etree.HTML，将字符串转化为Element对象
html = etree.HTML(text)

#1. 先分组取到一个同时包含标题和url的列表
ret3 = html.xpath("//li[@class='item-1']")
print(ret3) #[<Element li at 0xc24748>, <Element li at 0xc24808>, <Element li at 0xc242c8>]

# 2. 遍历列表，取其中每一个分组，进行数据提取，这样其实网页变化了保证了数据对应准确
for i in ret3:
    item = {}
    #<li class="item-1"><a href="link2.html">second item</a></li>
    # i是一个Element对象，Element对象可以用xpath（）方法，xpath（）方法返回值是一个列表。
    text_list = i.xpath("./a/text()") #获取当前li下a的内容
    item["title"] = text_list[0] if len(text_list) else None
    href_list = i.xpath("./a/@href") #获取当前li下a的url
    item["href"] = href_list[0] if len(href_list) else None
    print(item)