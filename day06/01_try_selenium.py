from selenium import webdriver
import time


# 实例化一个浏览器
# driver = webdriver.Chrome("C:\\Users\\Administrator\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe")
driver = webdriver.PhantomJS()

# 设置窗口大小
driver.set_window_size(1920,1080)
# 最大化窗口
driver.maximize_window()


#发送请求
driver.get("http://www.baidu.com")
#进行页面截屏
# driver.save_screenshot("./baidu.png")

# 元素定位的方法,send_keys()只能发送东西给input标签
# TODO find_element_by_id()定位的东西有多个怎么办，或者不是定位到input标签
driver.find_element_by_id("kw").send_keys("python")
driver.find_element_by_id("su").click()

#driver 获取html字符串
# print(driver.page_source) #浏览器中elements的内容

print(driver.current_url) #获取当前url,  click()之后的url

# # 获取cookie
# cookies=driver.get_cookies()
# print(cookies)
# print("-"*100)
#
# #把列表形式的cookies变成列表形式的cookies
# cookies = {i["name"]:i["value"] for i in cookies}
# print(cookies)

time.sleep(3)

driver.close() #关闭当前页面，当打开多个页面时，可能用
#退出浏览器
# driver.quit()

# C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\;rogram Files (x86)\Intel\OpenCL SDK\2.0\bin\x86;C:\Program Files (x86)\Intel\OpenCL SDK\2.0\bin\x64;C:\Program Files (x86)\NVIDIA Corporation\PhysX\Common;E:\Python工作软件\node\;E:\Python工作软件\mysql-5.7.22-winx64\bin;E:Python工作软件\Python3.5\Scripts;E:\Python工作软件\Python3.5\Lib\site-packages\django\bin;E:\Python工作软件\sqlite3;E:\Python工作软件\Redis\Redis-x64-3.2.100;E:\Python工作软件\HTML软件\GIT\Git\cmd;E:\Python工作软件\Python3.5;E:\Python工作软件\Python3.5\Scripts;C:\Users\Administrator\AppData\Local\Google\Chrome\Application;