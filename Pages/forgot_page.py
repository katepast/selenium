from selenium.webdriver.common.by import By
from Pages.base_page import BasePage


class ForgotPage(BasePage):

   """
   Locators and actions on the home Page
   """
   FORGOT_LINK = (By.XPATH,".//a[text()='Forgot account?']")
   FORGOT_TITLE = (By.XPATH,".//h2[text()='Find Your Account' and @class = 'uiHeaderTitle']")
   PHONE_OR_EMAIL_FIELD = (By.ID, "identify_email")
   SEARCH_BUTTON = (By.NAME,"did_submit")
   CANCEL_BUTTON = (By.XPATH,".//span[@class='uiButtonText']")
   VALIDATION_FORGOT_MESSAGE = (By.XPATH,".//div[@class='fsl fwb fcb']")


   def open_forgot_page(self):
       forgot_link = self.driver.find_element(*self.FORGOT_LINK)
       forgot_link.click()

   def is_forgot_account_link_displayed(self):
       forgot_link = self.driver.find_element(*self.FORGOT_LINK)
       return self.driver.wait_till_element_is_displayed(self.FORGOT_LINK,timeout=1)

   def is_forgot_title_correct_displyed(self):
       forgot_title = self.driver.find_element(*self.FORGOT_TITLE)
       assert forgot_title.text == "Find Your Account"

   def enter_invalid_data(self,invalid_value):
       invalid_data = self.driver.find_element(*self.PHONE_OR_EMAIL_FIELD)
       invalid_data.send_keys(invalid_value)

   def click_on_search_button(self):
       self.driver.find_element(*self.SEARCH_BUTTON).click()

   def get_error_message(self):
       return self.driver.find_element(*self.VALIDATION_FORGOT_MESSAGE).get_attribute('innerText')

   def clear_field(self):
       phone_email_field = self.driver.find_element(*self.PHONE_OR_EMAIL_FIELD)
       phone_email_field.clear()






