import selenium 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Edge()
driver.get('http://sci2020-af.bollore-logistics.com:81/bi/?perspective=home')
time.sleep(3)
driver.maximize_window()
driver.find_element("xpath","//input[@id='CAMUsername']").send_keys('SCI_AF')
driver.find_element("xpath","//input[@id='CAMPassword']").send_keys('SCI_AF')
driver.find_element("xpath","//button[@class='signInBtn']").click()
time.sleep(20)
driver.refresh()
time.sleep(10)
driver.find_element("xpath","//button[@id='com.ibm.bi.contentApps.teamFoldersSlideout']").click()
driver.implicitly_wait(5)
driver.find_element("xpath", "//tr[@data-name = 'SCI Platform']").click()
driver.implicitly_wait(5)
driver.find_element("xpath", "//div[@title='SCI Reports AF']").click()
driver.implicitly_wait(5)
driver.find_element("xpath", "//div[@title= 'MA']").click()
driver.implicitly_wait(5)
driver.find_element("xpath", "//div[@title= 'MA1']").click()
driver.implicitly_wait(5)
driver.find_element("xpath", "//div[@title= 'LMA New']").click()
driver.implicitly_wait(5)
driver.find_element("xpath", '//div[@aria-label = "Réception Management Rapport - Mois"]').click()
