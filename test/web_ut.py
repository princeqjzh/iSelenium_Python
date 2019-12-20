import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class ISelenium(unittest.TestCase):
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        config = self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        using_headless = os.environ["using_headless"]
        chrome_options = Options()
        if using_headless == 'true':
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       chrome_options=chrome_options)

    def test_webui_1(self):
        self.driver.get("https://ww.baidu.com")
        print('Open the browser, visit www.baidu.com')
        time.sleep(2)
        assert u"百度一下" in self.driver.title

        self.driver.maximize_window()
        print("Max the browser window")

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(u"今日头条" + Keys.RETURN)
        time.sleep(2)
        self.assertTrue(u"今日头条" in self.driver.title, msg='Verify test webui_1 pass')

    def test_webui_2(self):
        self.driver.get("https://ww.baidu.com")
        print('Open the browser, visit www.baidu.com')
        time.sleep(2)
        assert u"百度一下" in self.driver.title

        self.driver.maximize_window()
        print("Max the browser window")

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(u"王者荣耀" + Keys.RETURN)
        time.sleep(2)
        self.assertTrue(u"王者荣耀" in self.driver.title, msg='Verify test webui_2 pass')
