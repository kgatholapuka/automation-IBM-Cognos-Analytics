import time
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains


driver = webdriver.Edge()
driver.get('http://sci2020-af.bollore-logistics.com:81/bi/?perspective=home')
driver.implicitly_wait(60)
driver.maximize_window()
driver.find_element("xpath","//input[@id='CAMUsername']").send_keys('SCI_AF')
driver.find_element("xpath","//input[@id='CAMPassword']").send_keys('SCI_AF')
driver.find_element("xpath","//button[@class='signInBtn']").click()
driver.implicitly_wait(25)
time.sleep(10)
driver.find_element("xpath",'//*[@id="com.ibm.bi.contentApps.teamFoldersSlideout"]/div/div').click()
driver.implicitly_wait(5)
driver.find_element("xpath", "//div[@title='SCI Platform']").click()
driver.implicitly_wait(15)
driver.find_element("xpath", "//div[@title='SCI Reports AF']").click()
driver.implicitly_wait(10)
driver.find_element("xpath", "//div[@title= 'MA']").click()
driver.implicitly_wait(10)
driver.find_element("xpath", "//div[@title= 'MA1']").click()
driver.implicitly_wait(10)
driver.find_element("xpath", "//div[@title= 'LMA New']").click()
#sort By close the window
driver.find_element("xpath",'//button[@title = "Sort"]').click() 
driver.find_element("xpath",'//*[@id="com.ibm.bi.contentApps.teamFoldersSlideout.bi/content_apps/LegacyCATeamFoldersView.global"]/div[6]/div/div[4]/div/div[2]/span/ul[2]/li[2]/div[1]').click()
#sort By close the window
driver.find_element("xpath",'//button[@title = "Sort"]').click() 
driver.implicitly_wait(20)
#driver.find_element("xpath", '//tr[@data-name= "Réception Management Rapport - Mois"]').click()
action = ActionChains(driver)
action.double_click(driver.find_element("xpath", '//tr[@data-name= "Réception Management Rapport - Mois"]')).perform()
print("Report has been downloaded")
time.sleep(40)
