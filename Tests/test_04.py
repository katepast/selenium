import unittest
from time import time, sleep

from Pages.forgot_page import ForgotPage
from Tests.base_test import BaseTest


class TestClickForgotTest(BaseTest):

    def test_addPost(self):

        forgot_page = ForgotPage(self.driver)
        forgot_page.open_forgot_page()
        forgot_page.is_forgot_title_correct_displyed()

