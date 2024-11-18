# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 09:38:19 2024

@author: Lasse
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 12:55:29 2024

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

import pandas as pd

page_url = "https://www.basiqdental.dk/da_DK/"
# data = pd.read_excel(r"c:\users\lasse\onedrive\skrivebord\potential-in-action\web-scraping\Data Cliniclands 24.10.2024")
# artikel_numre = data["Cliniclands varenr."]
# artikel_descriptions = data["Cliniclands beskrivelse"]

# artikel_start = 452
# artikel_end = 469

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(page_url)

# shadow_host = driver.find_element(By.ID, "usercentrics-root"); shadow_host.size
# shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
# cookies_button = shadow_root.find_element(By.CSS_SELECTOR, '[data-testid=uc-accept-all-button]')
# cookies_button.click()

time.sleep(4)

try:
    cookies_button = driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    cookies_button.click()
except NameError:
    print("No Cookies Window")


searchbar = driver.find_element(By.CLASS_NAME,"searchbox")
searchbar.send_keys("473500");
searchbar.send_keys(Keys.ENTER)

bd = driver.find_element(By.CLASS_NAME,"bd")
bd.size
bd_content = bd.find_element(By.CLASS_NAME,"m2d-body-content");bd_content.size#search_results = bd_content.find_element(By.XPATH,"//cx-page-layout[@class='SearchResultsListPageTemplate ng-star-inserted']")


product = search_results.find_element(By.XPATH,"//m2d-product-list-item[@class='cx-product-search-list ng-star-inserted']")

product.click()

description = driver.find_element(By.TAG_NAME,"h1")

print(description.text)
