from config import Config
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
import time
import os

LOCATOR_GMAIL_LOGIN_AREA = "identifier"
LOCATOR_GMAIL_LOGIN_BUTTON = "button.VfPpkd-LgbsSe"
LOCATOR_GMAIL_PASSWORD_AREA = "password"
class Log:
    def enter_login(login):
        login_area = Config.Driver.find_element(By.NAME, LOCATOR_GMAIL_LOGIN_AREA)
        login_area.send_keys(login)

    def click_on_the_button():
        Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_LOGIN_BUTTON).click()
        Config.Driver.implicitly_wait(10)
        time.sleep(2)

    def enter_password(password):
        PasswordArea= Config.Driver.find_element(By.NAME, LOCATOR_GMAIL_PASSWORD_AREA)
        PasswordArea.send_keys(password)
