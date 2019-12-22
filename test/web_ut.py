import configparser
import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options


class ISelenium(unittest.TestCase):
    # 读入配置文件
    def get_config(self):
        config = configparser.ConfigParser()
        config.read(os.path.join(os.environ['HOME'], 'iselenium.ini'))
        return config

    def tearDown(self):
        self.driver.quit()

    def setUp(self):
        config = self.get_config()

        # 控制是否采用无界面形式运行自动化测试
        try:
            using_headless = os.environ["using_headless"]
        except KeyError:
            using_headless = None
            print('没有配置环境变量 using_headless, 按照有界面方式运行自动化测试')

        chrome_options = Options()
        if using_headless is not None and using_headless.lower() == 'true':
            print('使用无界面方式运行')
            chrome_options.add_argument("--headless")

        self.driver = webdriver.Chrome(executable_path=config.get('driver', 'chrome_driver'),
                                       chrome_options=chrome_options)

    def test_webui_1(self):
        self.driver.get("https://ww.baidu.com")
        print('打开浏览器，访问 www.baidu.com')
        time.sleep(5)
        assert u"百度一下" in self.driver.title

        self.driver.maximize_window()
        print("浏览器窗口最大化")

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(u"今日头条" + Keys.RETURN)
        print('搜索关键词~今日头条')
        time.sleep(5)
        self.assertTrue(u"今日头条" in self.driver.title, msg='webui_1校验点 pass')

    def test_webui_2(self):
        self.driver.get("https://ww.baidu.com")
        print('打开浏览器，访问 www.baidu.com')
        time.sleep(5)
        assert u"百度一下" in self.driver.title

        self.driver.maximize_window()
        print("浏览器窗口最大化")

        elem = self.driver.find_element_by_name("wd")
        elem.send_keys(u"王者荣耀" + Keys.RETURN)
        print('搜索关键词~王者荣耀')
        time.sleep(5)
        self.assertTrue(u"王者荣耀" in self.driver.title, msg='webui_1校验点 pass')
