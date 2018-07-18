from selenium import webdriver


class BasePage(object):

    def __init__(self, driver):
        self.driver = driver
        # driver.get('https://uk-ua.facebook.com/')

    def open(self):
        self.driver.get('https://uk-ua.facebook.com/')