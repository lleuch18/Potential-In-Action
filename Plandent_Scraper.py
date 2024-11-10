# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 11:13:49 2024

@author: Lasse
"""

import requests
from bs4 import BeautifulSoup
import sys
import time
import random

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import pandas as pd

page_url = "https://plandent.dk/"
# data = pd.read_excel(r"c:\users\lasse\onedrive\skrivebord\potential-in-action\web-scraping\Data Cliniclands 24.10.2024")
# artikel_numre = data["Cliniclands varenr."]
# artikel_descriptions = data["Cliniclands beskrivelse"]

# artikel_start = 452
# artikel_end = 469

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(page_url)

# Setup wait for later
wait = WebDriverWait(driver, 10)

#Save Original Tab Handle
original_window = driver.current_window_handle

#Accept Cookies
try:
    cookie_menu = driver.find_element(By.CLASS_NAME,"coi-button-group")
    accept_button = cookie_menu.find_element(By.CLASS_NAME,"coi-banner__accept")
    accept_button.click()
except NameError:
    print("No Cookies Menu")

#Find Searchbar
searchbar = driver.find_element(By.CLASS_NAME,"header__search").find_element(By.XPATH,"//div[@class='search-bar']")

#Switch Search from Articles to Products
#Locate and click on dropdown menu
searchbar_dropdown = searchbar.find_element(By.XPATH,"div[@class='search-bar__dropdown dropdown']")
searchbar_dropdown.click()
searchbar_dropdown_show = searchbar.find_element(By.XPATH,"div[@class='search-bar__dropdown dropdown show']")
#Select Articles
searchbar_articles_button = searchbar_dropdown_show.find_element(By.XPATH, "div[@class='search-bar__dropdown-menu dropdown-menu']").find_element(By.XPATH,"//a[contains(text(),\'Produkter')]")  
searchbar_articles_button.click()

#Input Article nr. to search form
searchbar_input = driver.find_element(By.CLASS_NAME,"search-bar__input")
searchbar_input.send_keys('19504')
searchbar_button = searchbar_input.find_element(By.XPATH,"//button[@class='search-bar__submit']")

searchbar_button.click()

#Wait for new window to open
wait.until(EC.number_of_windows_to_be(2))

#Loop thorugh window handles in driver untill one new window is reached
for window_handle in driver.window_handles:
    if window_handle != original_window:
        driver.switch_to.window(window_handle)
        break

#Remove Popup
#Locate Shadowhost
shadow_host = driver.find_element(By.XPATH,"//*[starts-with(name(),'sleeknote-') and contains(name(),'top')]")
shadow_host.size

shadow_host = driver.find_element(By.XPATH, "//*[@id='aspnetForm']")
test=driver.find_element(By.XPATH,"/html/body/sleeknote-q4qx0s-top")
shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
cookies_button = shadow_root.find_element(By.CSS_SELECTOR, '[data-testid=uc-accept-all-button]')
cookies_button.click()
    

articles = driver.find_element(By.CLASS_NAME,"articles")
articles_list = articles.find_element(By.CLASS_NAME,"articles-result")
description = articles_list.find_element(By.CLASS_NAME,"truncate")

print(description.text)
