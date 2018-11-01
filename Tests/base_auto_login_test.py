import unittest
from time import time

from Pages.fb_login_page import FBPage
from Tests.base_test import BaseTest


class BaseAutoLoginTest(BaseTest):

    def setUp(self):
        super().setUp()
        fb_page = FBPage(self.driver)
        fb_page.login_to_fb(fb_page.email, fb_page.password)


    def tearDown(self):
        self.driver.save_screenshot(
            "C:\\Users\\kate.pastbina\\Desktop\\FBTest\\Screenshots\\screen_%s_%s.png" % (
                self.__class__.__name__, time()))
        self.driver.quit()

