# -*- coding: utf-8 -*-
import wget
#from urllib.request import urlretrieve
import requests

from tqdm import tqdm

from datetime import datetime
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select


#Config sele_chrome.py for DAIWA
"""
USAGE:
/home/gci/GCI $ python sele_chrome.py 


"""


def main():
  #DAIWA CONFIG
  url = "https://lzone.daiwa.co.jp/lzone/"
  username = "shinichiro.ueno@gci.jp"
  password = "gcigci"
  
  

  #Ticker
  ticker_list = []
  
  def get_ticker(ticker_list):
    for ticker in ticker_list:
		yield ticker


  ticker = get_ticker(ticker_list)

  #Period
  period_pair = (("2011/04/01","2012/03/31"),("2012/04/01","2013/03/31"),("2013/04/01","2014/03/31"),("2014/04/01","2015/03/31"),("2015/04/01","2016/03/01"))

  def get_period(period_pair):
    for period in period_pair:
		yield period[0],period[1]

  period_from = "2011/04/01"
  period_to = "2016/03/31"
  


  file_type = 2
  
  #Run Method

  #Set WebDriver Chrome
  chromeOptions= webdriver.ChromeOptions()
  prefs = {"plugins.plugins_list":[{"enabled":False,"name":"Chrome PDF Viewer"}],"download.prompt_for_download":False,"safebrowsing.enabled":True,"extensions_to_open":""}
  chromeOptions.add_experimental_option("prefs",prefs)
  driver = webdriver.Chrome(executable_path = '/home/gci/Downloads/chromedriver',chrome_options=chromeOptions)
  
  #Run
  driver.get(url)
  driver.maximize_window()
  time.sleep(3)

  #Page 
  driver.find_element_by_id('ticker').send_keys(Keys.ENTER)
  driver.find_element_by_id('input-text').send_keys("3382")
  driver.find_element_by_id('input-btn-se').send_keys(Keys.ENTER)
  time.sleep(1)
  
  #Login Page
  driver.find_element_by_css_selector('input[name="memberId"]').send_keys(username)
  driver.find_element_by_css_selector('input[name="passWord"]').send_keys(password)
  driver.find_element_by_id('image-btn_ok').send_keys(Keys.ENTER)
  time.sleep(1)
  
  #Search 
  driver.find_element_by_id('ticker').send_keys(Keys.ENTER)
  driver.find_element_by_id('input-text').send_keys("3382")
  driver.find_element_by_id('input-btn-ad').send_keys(Keys.ENTER)
  time.sleep(1)

  #Search and Loop
  period_from, period_to = get_period(period_pair)
  ticker = get_ticker(ticker_list)


  elements = driver.find_elements_by_css_selector("input[type ='radio'][value='equity']")
  for element in elements:
	  element.click()
  driver.find_element_by_name('model.tickerCd').send_keys(ticker)
  select = Select(driver.find_element_by_name('model.docType'))
  select.select_by_value("2")
  driver.find_element_by_id('date1').send_keys(10*Keys.BACKSPACE)
  driver.find_element_by_id('date1').send_keys(period_from)
  driver.find_element_by_id('date2').send_keys(10*Keys.BACKSPACE)
  driver.find_element_by_id('date2').send_keys(period_to)
  time.sleep(2)
  driver.find_element_by_id('image-btn_search').send_keys(Keys.ENTER)
  time.sleep(1)

  #Result Page
  elements = driver.find_elements_by_css_selector("a[onclick*=pdfdownload]")
  
  num = 0
  time.sleep(1)
  
  #TODO Rename PDF FILES

  for element in elements:
	element.click()
	pdf_link = driver.current_url
	#urllib.urlretrieve(pdf_link,"DAIWA"+str(3382)+"_"+num)
	time.sleep(5)
	num +=1
	print "Done"
	
	time.sleep(3)
	
	print "Now"
	
	
	time.sleep(3)
	time.sleep(3)
  print "Finish!!!"
  
  driver.close()

if "__name__" == ""__main__"":
main()
