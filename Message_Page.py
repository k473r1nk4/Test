from config import Config
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

LOCATOR_GMAIL_SUBJECT = '.ha>.hP'
LOCATOR_GMAIL_BODY = '.a3s'
LOCATOR_GMAIL_DOWNLOAD_FILE = '.akn'
LOCATOR_GMAIL_NAME_FILE = '.aV3'

class MessagePage:

    def check_subject():
        subject = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_SUBJECT).text
        if subject == Config.SubjectToMail:
            print("Subject success")
        else:
            print("sad")
        time.sleep(3)

    def check_body():
        body = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_BODY).text
        if body == Config.BodyMail:
            print("Body success")
        else:
            print("sad")

    def download_file():
        Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_DOWNLOAD_FILE).click()

    def check_file():
        path = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_NAME_FILE).text
        time.sleep(15)
        fileOp="C:\\Users\\Katya\\Downloads\\"+path
        if open(fileOp).read() == open(Config.PathFile).read():
            print("File success")
        else:
            print("sad")
        os.remove(fileOp)