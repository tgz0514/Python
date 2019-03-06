import re

a = 'http:\\/\\/www.cssxt.com\\/uploadfile\\/2017\\/1208\\/20171208110834538.jpg'
a="""
"obj_url":"http:\/\/img6.2345.com\/zmimg\/img\/paperList\/25\/1080_1920\/2345LSPaper1080_19201406353231.jpeg?VendorID=2345&ResourceID=10162&ResourceName=3&ResourceIconUrl=2345&ResourceType=Wallpaper"
"""
pic_url = re.findall(r'"obj_url":"[^\\]*"', a, re.S)
print(pic_url)

# b = re.findall(r"[^\\]*",a)
# print(b)
# b="".join(b)
# print(b)

# b = re.sub(r'\\','',a)
# print(b)
