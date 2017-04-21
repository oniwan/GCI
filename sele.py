from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time


driver = webdriver.PhantomJS()
url = "https://lzone.daiwa.co.jp/lzone/common/authorize"
username='shinichiro.ueno@gci.jp'
password = 'gcigci'
driver.get(url)
driver.save_screenshot('search_result2.png')
print driver.current_url

driver.find_element_by_css_selector('input[name="memberId"]').send_keys(username)
driver.find_element_by_css_selector('input[name="passWord"]').send_keys(password)
driver.save_screenshot('search_result3.png')
#driver.find_element_by_class_name('button-login').send_keys(Keys.ENTER)
driver.find_element_by_id('image-btn_ok').send_keys(Keys.ENTER)

print driver.current_url
driver.save_screenshot('search_result410.png')
'''
wait = WebDriverWait(driver, 10)

driver.get(url)
print driver.current_url

driver.save_screenshot('search_result1.png')
driver.find_element_by_css_selector('input[name="account"]').send_keys(username)
driver.find_element_by_css_selector('input[name="password"]').send_keys(password)
driver.find_element_by_class_name('button-login').send_keys(Keys.ENTER)

time.sleep(10)
print driver.current_url

driver.save_screenshot('search_result2.png')



print "end"
'''
