import unittest
from selenium import webdriver
from Pages.base_page import BasePage
from Pages.fb_page import FBPage

class TestLoginFb(unittest.TestCase):

    MYPWD = "1234"

    def setUp(self):
        self.driver = webdriver.Chrome('C:\\Users\\kate.pastbina\\Desktop\\FB\\drivers\\chromedriver.exe')
        self.driver.maximize_window()

    def test_FBlogin(self):
        fb_page = FBPage(self.driver)
        fb_page.open()
        fb_page.enter_email()
        fb_page.enter_password()
        fb_page.signin()
        fb_page.is_avatar_displayed()

    def tearDown(self):
        self.driver.quit()
