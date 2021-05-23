from Message_Page import MessagePage
from New_User_Page import NewUser
from config import Config
from Login_Page import Log
from Main_Page import MainPage
from selenium import webdriver
import time
import os


def Autorisation(login, password):
    Log.enter_login(login)
    Log.click_on_the_button()
    time.sleep(2)
    Log.enter_password(password)
    Log.click_on_the_button()
    time.sleep(4)

def FillLetterAndSend(to, subject, body, fileIn):
    MainPage.write_message()
    MainPage.enter_to(to)
    MainPage.enter_subject(subject)
    MainPage.enter_message(body)
    MainPage.input_file(fileIn)
    MainPage.send_message()

def Out():
    Config.Driver.get("https://accounts.google.com/Logout?hl=ru&continue=https://mail.google.com/mail&service=mail&timeStmp=1614707093&secTok=.AG5fkS-nezExemFRLoLaoCP449zXWWxQrw&ec=GAdAFw")

def OpenMessage():
    MainPage.open_message()

def Check():
    MessagePage.check_subject()
    MessagePage.check_body()
    MessagePage.download_file()
    MessagePage.check_file()


try:
    Config.browser()
    Autorisation(Config.LoginFirst, Config.PasswordFirst)
    FillLetterAndSend(Config.LoginSecond, Config.SubjectToMail, Config.BodyMail, Config.PathFile)
    Out()
    time.sleep(2)
    NewUser.chose_new_user()
    Autorisation(Config.LoginSecond, Config.PasswordSecond)
    OpenMessage()
    Check()
finally:
    Config.Driver.quit()
