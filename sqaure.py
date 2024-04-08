import time
import pytest
import selenium
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver import ActionChains

driver = webdriver.Edge()
driver.get('http://square2016-af.bollore-logistics.com:12000/manh/index.html?i=82')
driver.implicitly_wait(60)
driver.find_element("xpath", "//input[@id='textfield-1019-inputEl']").send_keys("KPuka")
driver.find_element("xpath","//input[@id='textfield-1020-inputEl']").send_keys("Puka123")
driver.find_element("xpath", '//*[@id="button-1022-btnWrap"]').click()
# not working but we have to use double click for this element
action = ActionChains(driver)
action.double_click(driver.find_element("xpath", '//*[@id="proceed-button"]')).perform()
action.double_click(driver.find_element("xpath", '//*[@id="proceed-button"]')).perform()
driver.find_element("xpath",'//*[@id="mps_regions_selector-1056-btnIconEl"]').click()
driver.find_element("xpath",'//*[@id="combobox-1058-trigger-picker"]').click()
driver.find_element("xpath",'//*[@id="boundlist-1059-listEl"]/li[3]').click()
driver.find_element("xpath",'//*[@id="combobox-1060-trigger-picker"]').click()     
driver.find_element("xpath",'//*[@id="boundlist-1061-listEl"]/li[15]').click()
driver.find_element("xpath",'//*[@id="button-1064-btnInnerEl"]').click()

# Menu page
driver.find_element("xpath",'//*[@id="button-1013-btnIconEl"]').click()
driver.find_element("xpath",'//*[@id="button-1085-btnInnerEl"]').click()
driver.find_element("xpath",'//*[@id="tab-1109-btnInnerEl"]').click()
driver.find_element("xpath", '//*[@id="component-1098"]/div[6]/div[2]').click()

# ASN input
time.sleep(15)
driver.find_element("xpath", "/html/body/div[15]/div[2]/div/div/div[2]/div/div[6]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[2]").click()
driver.find_element("xpath","//div[@class='mps-filter-combo-option']").click()
l = ['24R47806', '0240600449', '0240600362', '24R12032', '24R2726', '0240600849', '0240600848', '0240600505', '24R5630', '0240600341', '0240600165', '0240600687', '0240600506', '0240601133']
for asn in l:
    text_input = driver.find_element("xpath",'/html/body/div[14]/div[2]/div/div/div[2]/div/div[6]/div[2]/div/div/div[2]/div/div/div[2]/div[2]/div/div/div[1]/div/div/div/div/div/div[3]/div/div/div/div/div/div/div/div[1]/input')

    text_input.clear()

    text_input.send_keys(asn)

    driver.find_element("xpath",'/html/body/div[14]/div[2]/div/div/div[2]/div/div[6]/div[3]/div[2]/div/a[2]/span/span/span[2]').click()

    print(driver.find_element("xpath","//td[@class='x-grid-cell x-grid-td x-grid-cell-status x-grid-cell-last']").text)
