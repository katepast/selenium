import pytest
from Pages.profile_page import ProfilePage
from Tests.base_auto_login_test import BaseAutoLoginTest


class TestOpenCheckinPage():

    def test_profile_page(self, login_fb):
        profile_page = ProfilePage(login_fb)
        profile_page.click_on_profile_button()
        profile_page.open_more_combobox()
        profile_page.select_chekins_option()
        profile_page.is_displayed_checkins_title()