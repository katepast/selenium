from selenium.webdriver.common.by import By

from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

from Pages.profile_page import ProfilePage
from helpers.CommonActions import CommonActions
from helpers.data_generator import get_random_string


class HomePage(BasePage):
    """
    Locators and actions on the home Page
    """

    HOME_LINK = (By.LINK_TEXT, 'Home')
    ADD_POST_BUTTON = (By.XPATH, ".//span[text()='Compose Post']")
    SHARE_BUTTON = (By.XPATH, '//button[@data-testid="react-composer-post-button"]')
    POST_FIELD = (By.XPATH, "//br[@data-text='true']/ancestor::div[@role='presentation']//div[@aria-autocomplete='list']")
    POST_BY_TEXT = ".//p[text()='%s']"
    PROFILE_BUTTON = (By.XPATH,".//span[@class='_1vp5']")
    SETTINGS_BUTTON = (By.XPATH,".//div[@id='u_ps_0_0_d']/a[@data-testid='post_chevron_button']")
    #SETTINGS_BUTTON = (By.XPATH,".// div[@class ='_6a '] / a[@ data-testid='post_chevron_button']")
    DROP_DOWN_SETTINGS = (By.XPATH,".//ul[@class='_54nf']")
    SAVE_POST_OPTION = (By.XPATH, ".//div[@class='_2ezy']")
    UNSAVED_POST = (By.XPATH,".//div[@class='_2ezy' and text()='Unsave post']")

    def click_on_home_button(self):
        home_button = self.driver.find_element(*self.HOME_LINK).click()
        return HomePage(self.driver)

    def click_add_compose_post_button(self):
        add_post_button = self.driver.find_element(*self.ADD_POST_BUTTON)
        add_post_button.click()

    def add_post(self,value):
        add_post = self.driver.find_element(*self.POST_FIELD)
        add_post.send_keys(value)
        assert add_post.get_attribute('innerText') is not None
        print(add_post.get_attribute('innerText'))

    def click_share_button(self):
         self.driver.find_element(*self.SHARE_BUTTON).click()

    def is_post_present(self, post_text):
        loc = (By.XPATH, self.POST_BY_TEXT % post_text)
        return CommonActions.wait_till_element_present(self.driver, loc)

    def click_on_post_settings(self):
        self.driver.find_element(*self.SETTINGS_BUTTON).click()
        return CommonActions.wait_till_element_present(driver=self.driver, locator=(self.SETTINGS_BUTTON))

    def save_post(self):
        self.driver.find_element(*self.SAVE_POST_OPTION).click()

    def is_post_saved(self):
        unsaved_post = self.driver.find_element(*self.UNSAVED_POST)
        assert unsaved_post.text == "Unsaved post"

    def click_on_profile_button(self):
        profile_button = self.driver.find_element(*self.PROFILE_BUTTON).click()
        return ProfilePage(self.driver)







