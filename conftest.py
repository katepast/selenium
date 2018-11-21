from time import time
from configs import config
from selenium import webdriver
import pytest
from sys import platform
import os.path
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.fb_login_page import FBPage
from project import PROJECT_PATH


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument("--disable-notifications")
    #webdriver = None
    if platform == "win32":
        driver = webdriver.Chrome(os.path.join(PROJECT_PATH, "drivers", "chromedriver.exe"),
                                       chrome_options=options)
    elif platform == "darwin":
        driver = webdriver.Chrome('/Users/Kate/Desktop/FBTest/drivers/chromedriver', chrome_options=options)
    driver.implicitly_wait(3)
    yield driver
    driver.save_screenshot(
        "C:\\Users\\kate.pastbina\\Desktop\\FBTest\\Screenshots\\screen_%s_%s.png" % (
            driver.__class__.__name__, time()))
    driver.quit()

@pytest.fixture()
def open_fb(driver):
    fb_page = FBPage(driver)
    fb_page.open()
    yield driver

@pytest.fixture()
def login_fb(open_fb):
    fb_page = FBPage(open_fb)
    fb_page.login_to_fb(config.email, config.password)
    yield open_fb