import pytest
from selenium import webdriver
from Pages import fb_login_page
from Pages.fb_login_page import FBPage

"""Test data"""
email = 'pastbina1992@gmail.com'
password = 'PorscheGTS1623'

@pytest.fixture()
def launch_driver(request):
    driver = webdriver.Chrome('/Users/Kate/Desktop/FBTest/Tests/chromedriver')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture()
def driver_auto_login(request):
    fb_page = FBPage(request.cls.driver)
    fb_page = enter_password(*self.password)
    fb_page = enter_email(*self.email)
    fb_page = signin()
def signin(self):
    self.driver.find_element(*self.LOGIN_BUTTON).click()



def enter_email(self, *email):
    email_field = self.driver.find_element(*self.EMAIL_FIELD)
    email_field.send_keys(*self.email)

def enter_password(self, *password):
    password_field = self.driver.find_element(*self.PASSWORD_FIELD)
    password_field.send_keys(*self.password)

def signin(self):
    self.driver.find_element(*self.LOGIN_BUTTON).click()