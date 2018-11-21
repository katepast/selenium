import pytest
from Pages.forgot_page import ForgotPage
from Tests.base_test import BaseTest


class TestClickForgotTest(BaseTest):

    INVALID_DATA = 'invalid_text0123@'
    def test_addPost(self):

        forgot_page = ForgotPage(self.driver)
        forgot_page.open_forgot_page()
        forgot_page.enter_invalid_data(self.INVALID_DATA)
        forgot_page.clear_field()
        forgot_page.click_on_search_button()
        forgot_page.get_error_message()

        

