import pytest
from Pages.profile_page import ProfilePage
from Tests.base_auto_login_test import BaseAutoLoginTest


class TestOpenVideoPage(BaseAutoLoginTest):

    def test_profile_page(self):
        profile_page = ProfilePage(self.driver)
        profile_page.click_on_profile_button()
        profile_page.open_more_combobox()
        profile_page.select_videos_option()
        profile_page.is_displayed_video_title()



