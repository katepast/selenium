import unittest

from selenium import webdriver
from Pages.fb_login_page import FBPage
from Tests.base_auto_login_test import BaseAutoLoginTest


class TestLoginFb(BaseAutoLoginTest):

   def test_FBlogin(self):
        fb_page = FBPage(self.driver)
        assert fb_page.is_home_btn_present()
        assert fb_page.is_avatar_displayed()



