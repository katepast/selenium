from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class FBPage(BasePage):
    """
    Locators on FB Page
    """
    EMAIL_FIELD = (By.ID,'email')
    PASSWORD_FIELD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH,'//input[@data-testid="royal_login_button"]')
    AVATAR = (By.XPATH, "//span[@class='_1vp5']")
    HOME_LINK = (By.LINK_TEXT,'Home')

    """
    Test Data
    """
    email = 'pastbina1992@gmail.com'
    password = 'PorscheGTS1623'

    def __init__(self, driver):
        self.driver = driver
        # self.driver = webdriver.Chrome('/Users/Kate/Desktop/FBTest/Tests/chromedriver')
        self.driver.maximize_window()
        self.driver.save_screenshot('/Users/Kate/Desktop/FBTest/Tests/test_scr2.png')

    def enter_email(self):
         email_field = self.driver.find_element(*self.EMAIL_FIELD)
         email_field.send_keys('pastbina1992@gmail.com')

    def enter_password(self):
         password_field = self.driver.find_element(*self.PASSWORD_FIELD)
         password_field.send_keys('PorscheGTS1623')

    def signin(self):
         self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_avatar_displayed(self):
         avatar = self.driver.find_element(*self.AVATAR)
         return avatar.text == "Ekaterina"

    def click_on_home_button(self):
        home_button = self.driver.find_element(*self.HOME_LINK).click()








