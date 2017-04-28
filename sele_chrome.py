# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import time
from selenium.webdriver.support.ui import Select
#Config Sele_Chrome at DAIWA
url = "https://lzone.daiwa.co.jp/lzone/"
username = "shinichiro.ueno@gci.jp"
password = "gcigci"
ticker = 3382
period_from = "2011/04/01"
period_to = "2017/04/28"
file_type = 2

#Set WebDriver Chrome
driver = webdriver.Chrome(executable_path = '/home/gci/Downloads/chromedriver')

#wait = WebDriverWait(driver,10)
#Run
driver.get(url)
print driver.current_url

time.sleep(5)

driver.find_element_by_id('ticker').send_keys(Keys.ENTER)
driver.find_element_by_id('input-text').send_keys(ticker)
driver.find_element_by_id('input-btn-se').send_keys(Keys.ENTER)
time.sleep(3)
driver.save_screenshot('DAIWA_test1.png')


print driver.current_url

driver.save_screenshot('DAIWA_test2.png')
driver.find_element_by_css_selector('input[name="memberId"]').send_keys(username)
driver.find_element_by_css_selector('input[name="passWord"]').send_keys(password)
driver.save_screenshot('DAIWA_test3.png')
driver.find_element_by_id('image-btn_ok').send_keys(Keys.ENTER)
driver.save_screenshot('DAIWA_test4.png')

time.sleep(3)

driver.find_element_by_id('ticker').send_keys(Keys.ENTER)
driver.find_element_by_id('input-text').send_keys(ticker)
driver.find_element_by_id('input-btn-ad').send_keys(Keys.ENTER)
driver.save_screenshot('DAIWA_test5.png')

time.sleep(3)

driver.save_screenshot('DAIWA_test6.png')

elements = driver.find_elements_by_css_selector("input[type ='radio'][value='equity']")
for element in elements:
    element.click()
driver.find_element_by_name('model.tickerCd').send_keys(ticker)
#driver.find_element_by_id('model_periodFrom').send_keys(Keys.CONTROL,"a")
driver.find_element_by_id('date1').send_keys(10*Keys.BACKSPACE)
driver.find_element_by_id('date1').send_keys(period_from)
select = Select(driver.find_element_by_name('model.docType'))
select.select_by_value("2")
time.sleep(2)
#all_options = element.find_elements_by_tag_name("option")
#all_options[1].click()
driver.find_element_by_id('image-btn_search').send_keys(Keys.ENTER)

time.sleep(10)

driver.save_screenshot('DAIWA_test7.png')


driver.close()
