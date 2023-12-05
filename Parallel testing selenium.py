#We will use pytest in order to do parallel testing 

import pytest
from selenium imort webdriver


@pytest.fixture(scope="class")
def driver_init_1(request):
    web_driver = webdriver.Edge()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.fixture(scope="class")
def driver_init_2(request):
    web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from time import sleep
import sys
@pytest.mark.usefixtures("driver_init_1")

class BasicTest:

    pass

class Test_URL_Chrome(BasicTest):

    def test_lambdatest_todo_app(self):
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        self.driver.maximize_window()
        self.driver.find_element_by_name("li1").click()
        self.driver.find_element_by_name("li2").click()
        title = "Sample page - lambdatest.com"
        assert title ==  self.driver.title
        sample_text = "Happy Testing at LambdaTest"
        email_text_field =  self.driver.find_element_by_id("sampletodotext")
        email_text_field.send_keys(sample_text)
        time.sleep(5)
        self.driver.find_element_by_id("addbutton").click()
        time.sleep(5)
        output_str =  self.driver.find_element_by_name("li6").text
        sys.stderr.write(output_str)
        time.sleep(2)
       
    def test_lambdatest_load(self):
        self.driver.get('https://www.lambdatest.com/')
        self.driver.maximize_window()
        expected_title = "cross-browser Testing Tools | Free Automated Website Testing | LambdaTest"
        assert expected_title ==  self.driver.title
        time.sleep(5)
