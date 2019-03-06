from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://mail.qq.com")

#iframe框架把页面分成两个网页时，要先切换到iframe
driver.switch_to.frame("login_frame")

driver.find_element_by_id("u").send_keys("634369618")
time.sleep(3)
driver.quit()