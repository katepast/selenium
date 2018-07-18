import unittest
from time import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.base_page import BasePage
from Pages.fb_login_page import FBPage


class BaseAutoLoginTest(unittest.TestCase):

    def __init__(self, driver):
        super().__init__(driver)
        options = Options()
        options.add_argument("--disable-notifications")
        # self.driver = webdriver.Chrome('/Users/Kate/Desktop/FBTest/Tests/chromedriver')
        self.driver = webdriver.Chrome('drivers\\chromedriver.exe', chrome_options=options)
        self.driver.maximize_window()

    def setUp(self):
        fb_page = FBPage(self.driver)
        fb_page.open()
        fb_page.enter_email()
        fb_page.enter_password()
        fb_page.signin()

    def tearDown(self):
        self.driver.save_screenshot(
            "C:\\Users\\kate.pastbina\\Desktop\\FBTest(101)\\FBTest\\Tests\\screen_%s_%s.png" % (
            self.__class__.__name__, time()))
        self.driver.quit()
