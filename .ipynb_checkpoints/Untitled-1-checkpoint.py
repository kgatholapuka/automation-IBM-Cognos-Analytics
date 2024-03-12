# %%
import time
from selenium import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# %% [markdown]
# ## IBM Cognos Analytics (Report)

# %% [markdown]
# The following code opens a new window in Microsoft Edge.
#  Then visit the link and enter your username and  password.
#  Next, navigate to and download the “Reception Management Relationship – Mois” report.

# %%
driver = webdriver.Edge()
driver.get('http://sci2020-af.bollore-logistics.com:81/bi/?perspective=home')
driver.implicitly_wait(60)
driver.maximize_window()

# %%
driver.find_element("xpath","//input[@id='CAMUsername']").send_keys('SCI_AF')

# %%
driver.find_element("xpath","//input[@id='CAMPassword']").send_keys('SCI_AF')

# %%
driver.find_element("xpath","//button[@class='signInBtn']").click()

# %%
driver.find_element("xpath","//button[@id='com.ibm.bi.contentApps.teamFoldersSlideout']").click()

# %%
driver.find_element("xpath", "//tr[@data-name = 'SCI Platform']").click()

# %%
driver.find_element("xpath", "//div[@title='SCI Reports AF']").click()

# %%
driver.find_element("xpath", "//div[@title= 'MA']").click()

# %%
driver.find_element("xpath", "//div[@title= 'MA1']").click()

# %%
driver.find_element("xpath", "//div[@title= 'LMA New']").click()

# %%
driver.find_element("xpath", '//div[@aria-label = "Réception Management Rapport - Mois"]').click()

# %% [markdown]
# ## Manhattan (Square)


