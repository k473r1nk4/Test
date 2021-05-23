from selenium import webdriver
import time
import os

class Config:
    Driver = webdriver.Chrome()
    Driver.set_page_load_timeout(30)
    File = open("date.txt","r")
    SubjectToMail= File.readline().replace("\n", "")
    BodyMail=File.readline().replace("\n", "")
    PathFile=File.readline().replace("\n", "")
    File = open("log1.txt","r")
    LoginFirst=File.readline().replace("\n","")
    PasswordFirst=File.readline().replace("\n","")
    File = open("log2.txt","r")
    LoginSecond=File.readline().replace("\n","")
    PasswordSecond=File.readline().replace("\n","")

    def browser():
        Link= "https://accounts.google.com/AccountChooser?service=mail&continue=https://mail.google.com/mail/"
        time.sleep(2)
        Config.Driver.get(Link)
        time.sleep(2)
    

