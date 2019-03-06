from selenium import webdriver
import json
import time

class DouYuSpider:

    def __init__(self):
        self.url = "https://www.douyu.com/g_LOL"
        self.driver = webdriver.Chrome()

    def get_countent_list(self):
        li_list = self.driver.find_elements_by_xpath("//ul[@id='live-list-contentbox']/li")
        content_list = []
        for li in li_list:
            item = {}
            item["room_img_src"] = li.find_element_by_xpath(".//img[@class='JS_listthumb']").get_attribute("src")
            item["title"] = li.find_element_by_xpath("./a[@class='play-list-link']").get_attribute("title")
            item["room_type"] = li.find_element_by_xpath('.//span[@class="tag ellipsis"]').text
            item["anchor_name"] = li.find_element_by_xpath('.//span[@class="dy-name ellipsis fl"]').text
            item["watch_num"] = li.find_element_by_xpath('.//span[@class="dy-num fr"]').text
            content_list.append(item)
        print(content_list)
        # 获取写一页的元素
        next_page_element = self.driver.find_elements_by_xpath("//a[@class='shark-pager-next']")
        next_page_element = next_page_element[0] if len(next_page_element) else None
        return content_list, next_page_element

    def save_content_list(self,content_list):
        """4. 保存数据"""
        with open("./06斗鱼数据.txt","w",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=4))
                f.write("\n")
            print("保存成功")



    def run(self): #实现主要逻辑
        # 1. start_url
        # 2. 发送请求，获取响应
        self.driver.get(self.url)
        self.get_countent_list()
        # 3. 提取数据，且要提取下一页的元素
        content_list, next_page_element = self.get_countent_list()
        # 4. 保存数据
        self.save_content_list(content_list)

        # 5. 点击下一页，循环2-4
        while next_page_element is not None:
            next_page_element.click() #通过浏览器点击进入 下一页 超链接，这里是一个元素，也恰好是a标签超链接，可以点击跳转
            # 设置等待时间
            time.sleep(10) # 浏览器进入第二页以后，程序不在等待页面加载完成而继续执行。设置等待时间为了让页面加载完成，获取元素不报错
            content_list, next_page_element = self.get_countent_list()
            self.save_content_list(content_list)

        self.driver.quit() #退出浏览器
if __name__ == '__main__':
    douyu = DouYuSpider()
    douyu.run()