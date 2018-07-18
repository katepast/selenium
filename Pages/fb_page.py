from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Pages.base_page import BasePage

class FBPage(BasePage):
    """
    Locators on FB Page
    """
    EMAIL_FIELD = (By.ID,'email')
    PASSWORD_FIELD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH,'//input[@data-testid="royal_login_button"]')
    AVATAR = (By.XPATH, "//span[@class='_1vp5']")


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
         assert avatar.text == "Ekaterina"

