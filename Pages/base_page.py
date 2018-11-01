
class BasePage(object):

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        self.driver.get('https://www.facebook.com/')




