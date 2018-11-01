from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CommonActions():

    @staticmethod
    def wait_till_element_present(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        #return wait.until(EC.element_to_be_clickable(locator))
        try:
           return wait.until(EC.element_to_be_clickable(locator))
        except:
           return False

    @staticmethod
    def wait_till_text_present(driver, locator, timeout=10):
        wait = WebDriverWait(driver, timeout)
        try:
            return wait.until(EC.element_to_be_visible(locator),"Videos")
        except:
            return False


