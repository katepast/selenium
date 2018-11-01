import unittest
from time import time, sleep

from Pages.profile_page import ProfilePage

from Tests.base_auto_login_test import BaseAutoLoginTest


class TestOpenProfilePage(BaseAutoLoginTest):

    #VALUE = get_random_string(50)

    def test_profile_page(self):
        profile_page = ProfilePage(self.driver)
        profile_page.click_on_profile_button()

