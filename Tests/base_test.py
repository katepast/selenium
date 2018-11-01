import unittest
from time import time
from sys import platform
import os.path
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.base_page import BasePage
from Pages.fb_login_page import FBPage
from project import PROJECT_PATH


class BaseTest(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        options = Options()
        options.add_argument("--disable-notifications")

        if platform == "win32":
            self.driver = webdriver.Chrome(os.path.join(PROJECT_PATH, "drivers", "chromedriver.exe"), chrome_options=options)
        elif platform == "darwin":
            self.driver = webdriver.Chrome('/Users/Kate/Desktop/FBTest/drivers/chromedriver',chrome_options=options)
        # self.driver = webdriver.Chrome('/Users/Kate/Desktop/FBTest/Tests/chromedriver')
        #self.driver = webdriver.Chrome('drivers\\chromedriver.exe', chrome_options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)

    def setUp(self):
        fb_page = FBPage(self.driver)
        fb_page.open()


    def tearDown(self):
        self.driver.save_screenshot(
            "C:\\Users\\kate.pastbina\\Desktop\\FBTest\\Screenshots\\screen_%s_%s.png" % (
            self.__class__.__name__, time()))
        self.driver.quit()
