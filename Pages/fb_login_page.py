from selenium import webdriver
from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from Pages.forgot_page import ForgotPage
from Pages.home_page import HomePage
from helpers.data_generator import get_random_string
from helpers.CommonActions import CommonActions


class FBPage(BasePage):
    """
    Locators on FB Page
    """
    EMAIL_FIELD = (By.ID,'email')
    PASSWORD_FIELD = (By.ID, "pass")
    LOGIN_BUTTON = (By.XPATH,'//input[@data-testid="royal_login_button"]')
    PROFILE_BUTTON = (By.XPATH, "//span[@class='_1vp5']")
    #HOME_LINK = (By.LINK_TEXT,'Home')
    HOME_LINK = (By.XPATH, ".// a[text() = 'Home']")
    ADD_POST_BUTTON = (By.XPATH,".//span[text()='Compose Post']")
    SHARE_BUTTON = (By.XPATH,'//button[@data-testid="react-composer-post-button"]')
    POST_FIELD = (By.XPATH,"//br[@data-text='true']/ancestor::div[@role='presentation']//div[@aria-autocomplete='list']")
    FORGOT_LINK = (By.XPATH, ".//a[text()='Forgot account?']")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.maximize_window()
        wait = WebDriverWait(driver, 10)

    def login_to_fb(self, email, password):
        email_el = self.driver.find_element(*self.EMAIL_FIELD)
        email_el.send_keys(email)
        password_el = self.driver.find_element(*self.PASSWORD_FIELD)
        password_el.send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()
        return HomePage(self.driver)

    def is_avatar_displayed(self):
         avatar = self.driver.find_element(*self.PROFILE_BUTTON)
         return avatar.text == "Ekaterina"

    def is_home_btn_present(self):
        return CommonActions.wait_till_element_present(driver=self.driver, locator=(self.HOME_LINK))

    def click_on_home_button(self):
        home_button = self.driver.find_element(*self.HOME_LINK).click()
        return HomePage(self.driver)

    def open_forgot_page(self):
        forgot_link = self.driver.find_element(*self.FORGOT_LINK)
        forgot_link.click()
        return ForgotPage(self.driver)

    #def is_compose_post_form_displayed(self):
     #   wait = WebDriverWait(self.driver, 10)
     #  compose_post_form = wait.until(EC.presence_of_element_located(self.POST_FIELD))











