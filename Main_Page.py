from config import Config
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import os

LOCATOR_GMAIL_WRITE_MESSAGE_BUTTON = ".z0 .T-I"
LOCATOR_GMAIL_TO_AREA = ".eV>.oj .vO"
LOCATOR_GMAIL_SUBJECT_AREA = ".aoT"
LOCATOR_GMAIL_BODY_AREA = ".aoI .Am.Al"
LOCATOR_GMAIL_INPUT_FILE = "input[type=file]"
LOCATOR_GMAIL_SEND_BUTTON = ".btA .aoO"
LOCATOR_GMAIL_MESSAGE = 'td[role=gridcell]'

class MainPage:
    def write_message():
        Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_WRITE_MESSAGE_BUTTON).click()
        time.sleep(2)

    def enter_to(to):
        To = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_TO_AREA)
        To.send_keys(to)

    def enter_subject(subject):
        Subject = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_SUBJECT_AREA)
        Subject.send_keys(subject)

    def enter_message(body):
        LetterBody = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_BODY_AREA)
        LetterBody.send_keys(body)

    def input_file(fileIn):
        FileInput = Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_INPUT_FILE)
        FileInput.send_keys(fileIn)
        time.sleep(3)

    def send_message():
        Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_SEND_BUTTON).click()
        time.sleep(3)

    def open_message():
        Config.Driver.find_element(By.CSS_SELECTOR, LOCATOR_GMAIL_MESSAGE).click()
        time.sleep(3)

