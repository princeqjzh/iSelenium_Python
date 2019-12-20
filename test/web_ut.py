import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class ISelenium(unittest.TestCase):
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        config = self.get_config()
        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'))

    def test_webui_1(self):
        self.driver.get("https://ww.baidu.com")
        time.sleep(2)
        assert u"百度一下" in self.driver.title

        self.driver.maximize_window()

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(u"今日头条" + Keys.RETURN)
        time.sleep(2)
        assert u"今日头条" in self.driver.title

    def test_webui_2(self):
        self.driver.get("https://ww.baidu.com")
        time.sleep(2)
        assert u"百度一下" in self.driver.title

        self.driver.maximize_window()

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(u"王者荣耀" + Keys.RETURN)
        time.sleep(2)
        assert u"王者荣耀" in self.driver.title
