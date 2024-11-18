# -*- coding: utf-8 -*-
"""
Created on Tue Oct  8 18:28:14 2024

@author: Lasse
"""

#%% Imports
import requests
from bs4 import BeautifulSoup
import sys
import time
import Description_Module as dm
# #%% Cenger Scraper Raw
# #%%% Imports



# #%%% Set login_URL and login credentials for Cenger
# login_url = 'https://www.cenger.dk/varekatalog/3dfusion-wedge-100-stk-medium-orange'


# payload = {
#     "user": "86820601", 
#     "password": "torvet12",
# }


# #%%% Log in to Cenger
# response = requests.post(login_url, data=payload)




# #%%% Making a GET request
# r = requests.get(url)
# # check status code for response received
# # success code - 200
# if r.status_code == 200:
#     print(r)
# else: 
#     print("faulty request")
#     inp = input("Continue Y/N?")
#     if inp == "N":
#         sys.exit()


# #%%% Test BeautifulSoup
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
# print(soup.prettify())

# #%%% Extract Data from nested HTML structure

# s = soup.find('div', class_='phrase__container')
# content = s.find_all('p')

# print(s)#%% Cenger Scraper Selenium
#%% Cenger Scraper Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

import os
path = os.path.join("Users","Lasse","Onedrive","Skrivebord","Cenger_2.whtt")
# for holding the resultant list

#Login Credentials for Cenger
user_id = 86820601
password = "torvet12"

page_url = "https://www.cenger.dk/varekatalog/3dfusion-wedge-100-stk-large-groen"
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get(page_url)
#time.sleep(3)

#Content is the main section
content = driver.find_element(By.ID,"content1")

#Locate back_button within content
tilbage_knap = content.find_element(By.CLASS_NAME,"back")
#Get properties of back_button
tilbage_knap.location
tilbage_knap.size
#Click back_button
#tilbage_knap.click()



#Locate log_in button in row
#[1]cengerContainer/[DesktopSection/Content1/section productView/container customContainer/row/col-md-12/row/col-md-6/cold-md-12-loginForPrices
login_button = driver.find_element(By.XPATH,"html[1]/body[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")

#Locate login button element (Cookies need to be handled)
login_button.size
login_button.location
login_button.click()

#Locate the login_menu element
login_menu = driver.find_element(By.CLASS_NAME,"form")
login_menu.location
login_menu.size
#Locate the username label
id_label = login_menu.find_element(By.NAME,"Username")
id_label.size
#Locate the password label
password_label = login_menu.find_element(By.NAME,"Password")
password_label.size

#Send login credentials
id_label.send_keys(user_id)
password_label.send_keys(password)

#Locate login button within login form
column = driver.find_element(By.NAME,"ExtUserForm")
column.size
column.tag_name
#//Tagname[@AttibuteName = ‘value’]
#login_menu_button = column.find_elements(By.XPATH,'//form[contains(text(),"Log ind")]')#//ExtUserForm[@class="button"');
column.length
#login_menu_button = column.find_elements(By.XPATH,'.//form[@Class="button"]')
login_menu_button = column.find_element(By.CLASS_NAME,'button'); login_menu_button.size
login_menu_button.click()



cont = input("Close Chrome Session [Y/N]").upper()
if cont == "Y":
    #closing the driver
    driver.close()

dm.Locate_Description(page_url)
