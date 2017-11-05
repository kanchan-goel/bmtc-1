from bs4 import BeautifulSoup
import sys
import json
import requests

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

url="https://www.mybmtc.com/en"
driver = webdriver.Firefox()
driver.get(url)

elem = driver.find_element_by_id("quicktabs-tab-home_quick_tab_bottom-2")
elem.click()

elem = driver.find_element_by_id("fare_select_id")
elem.send_keys("A/C Service")

elem = driver.find_element_by_id("edit-submit--2")
elem.click()

WebDriverWait(driver, 50).until(EC.visibility_of_element_located((By.CLASS_NAME, "sticky-enabled tableheader-processed sticky-table"))) 

table =  driver.find_element_by_xpath('//*[@id="pub_fare_list_form"]/table[2]')
for row in table.find_element_by_xpath('//*[@id="pub_fare_list_form"]/table[2]/tbody/tr'):
    print([td.text for td in row.find_elements_by_xpath('//*[@id="pub_fare_list_form"]/table[2]/tbody/tr[row]/td')])
