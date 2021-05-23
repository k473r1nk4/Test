from config import Config
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

LOCATOR_GMAIL_NEW_USER = ".UXurCe"

class NewUser:
    def chose_new_user():
        Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_NEW_USER).click()
        time.sleep(2)

