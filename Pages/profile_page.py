from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from Pages.base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait

from helpers.CommonActions import CommonActions


class ProfilePage(BasePage):
    """
        Locators and actions on the Profile Page
    """
    PROFILE_BUTTON = (By.XPATH,".//span[@class='_1vp5']")
    MORE_BUTTON = (By.XPATH, ".//a[text()='More']")
    VIDEOS_OPTION = (By.XPATH, ".//a[@class='_54nc' and @data-tab-key='videos']")
    VIDEOS_TITLE = (By.XPATH, ".//a[text()='Videos']")
    PRESENCE_DROP_DOWN_BY_HOVER = (By.XPATH, ".//button[@class='hideToggler' and @type ='button']")
    CHEKINS_OPTION = (By.XPATH,".//li[@data-tab-key='map']//span[text()='Check-ins']")
    CHEKINS_TITLE = (By.XPATH, ".//a[text()='Check-ins']")
    option_main_xpath = ".//ul[@role = 'menu']//li[@data-tab-key='{}']"
    title_main_xpath = ".//a[text()='{}']"

    def click_on_profile_button(self):
        profile_button = self.driver.find_element(*self.PROFILE_BUTTON)
        profile_button.click()

    def open_more_combobox(self):
        if (CommonActions.wait_till_element_present(driver=self.driver, locator=(self.MORE_BUTTON))):
            more_btn = self.driver.find_element(*self.MORE_BUTTON)
            hover = ActionChains(self.driver).move_to_element(more_btn)
            hover.perform()
        else:
            print("MORE button is not displayed")

    def select_videos_option(self):
        if CommonActions.wait_till_element_present(driver=self.driver, locator=(self.VIDEOS_OPTION)):
           video_hover = self.driver.find_element(*self.VIDEOS_OPTION)
           video_hover.click()

    def is_displayed_video_title(self):
        if CommonActions.wait_till_element_present(driver=self.driver, locator=(self.VIDEOS_TITLE)):
           videos_title = self.driver.find_element(*self.VIDEOS_TITLE)
           assert videos_title.text == "Videos"

    def select_chekins_option(self):
        if CommonActions.wait_till_element_present(driver=self.driver, locator=(self.CHEKINS_OPTION)):
           chekins_hover = self.driver.find_element(*self.CHEKINS_OPTION)
           chekins_hover.click()

    def is_displayed_checkins_title(self):
        if CommonActions.wait_till_element_present(driver=self.driver, locator=(self.CHEKINS_TITLE)):
           chekins_title = self.driver.find_element(*self.CHEKINS_TITLE)
           assert chekins_title.text == "Check-ins"

    def select_sports_option(self):
        if CommonActions.wait_till_element_present(driver=self.driver, locator=(By.XPATH, self.option_main_xpath.format('sports'))):
           video_hover = self.driver.find_element(*self.option_main_xpath.format('sports'))
           video_hover.click()


    def is_displayed_sports_title(self):
       if CommonActions.wait_till_element_present(driver=self.driver, locator=(By.XPATH, self.title_main_xpath.format('Sports'))):
          videos_title = self.driver.find_element(*self.title_main_xpath.format('Sports'))
          assert videos_title.text == "Sports"