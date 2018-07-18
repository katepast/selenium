import unittest
from time import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from Pages.fb_login_page import FBPage
from Tests.base_auto_login_test import BaseAutoLoginTest


class TestLoginFb(BaseAutoLoginTest):

    def test_FBlogin(self):
        fb_page = FBPage(self.driver)
        fb_page.click_on_home_button()
