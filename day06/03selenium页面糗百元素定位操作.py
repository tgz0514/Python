from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.qiushibaike.com/")


# # find_element_by_xpath（）获取第一个div标签
# qiubai = driver.find_element_by_xpath('//div[contains(@class,"article block untagged mb15")]')
# print(qiubai)

# find_elements_by_xpath（）获取多个div标签
qiubai = driver.find_elements_by_xpath('//div[contains(@class,"article block untagged mb15")]')
print(qiubai)

for div in qiubai:
    #  find_elements_by_xpath（）只能获取到标签，不能获取标签属性，get_attribute()可以获取标签属性
    print(div.find_elements_by_xpath('.//a')[0].get_attribute("href"))
    #  find_elements_by_xpath（）只能获取到标签，不能获取标签内容
    print(div.find_element_by_xpath('.//div[@class="content"]/span').text)

#通过元素的内容，获取标签
print(driver.find_element_by_link_text("下一页")) #打印下一页selenium元素
print(driver.find_element_by_link_text("下一页").get_attribute("href")) #打印下一页的url

driver.quit()