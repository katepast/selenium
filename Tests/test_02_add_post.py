import unittest
from time import time, sleep

from Pages.fb_login_page import FBPage
from Pages.home_page import HomePage
from Tests.base_auto_login_test import BaseAutoLoginTest
from helpers.data_generator import get_random_string


class TestAddPost(BaseAutoLoginTest):

    VALUE = get_random_string(50)

    def test_addPost(self):
        home_page = HomePage(self.driver)
        home_page.click_on_home_button()
        sleep(3)
        home_page.click_add_compose_post_button()
        home_page.add_post(self.VALUE)
        home_page.click_share_button()
        assert home_page.is_post_present(self.VALUE)