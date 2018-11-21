import pytest
from time import time, sleep

from Pages.fb_login_page import FBPage
from Pages.home_page import HomePage
from Tests.base_auto_login_test import BaseAutoLoginTest
from helpers.data_generator import get_random_string


class TestAddPost(BaseAutoLoginTest):

    VALUE = get_random_string(50)

    def test_addPost(self):
        home_page = HomePage(self.driver)
        sleep(3)
        home_page.click_on_post_settings()
        sleep(2)
        home_page.save_post()
        # home_page.click_on_post_settings()
        # home_page.is_post_saved()