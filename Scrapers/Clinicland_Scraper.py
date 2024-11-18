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

page_url = "https://www.cliniclands.dk/"
# data = pd.read_excel(r"c:\users\lasse\onedrive\skrivebord\potential-in-action\web-scraping\Data Cliniclands 24.10.2024")
# artikel_numre = data["Cliniclands varenr."]
# artikel_descriptions = data["Cliniclands beskrivelse"]

# artikel_start = 452
# artikel_end = 469

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

driver.get(page_url)

shadow_host = driver.find_element(By.ID, "usercentrics-root"); shadow_host.size
shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
cookies_button = shadow_root.find_element(By.CSS_SELECTOR, '[data-testid=uc-accept-all-button]')
cookies_button.click()


page_content = driver.find_element(By.ID,"wrapper")
searchbar_box = page_content.find_element(By.ID,"search")
searchbar = searchbar_box.find_element(By.CLASS_NAME,"searchbar")
searchbar_form = searchbar_box.find_element(By.CLASS_NAME,"form")
searchbar_query = searchbar_form.find_element(By.CLASS_NAME,"query")

searchbar_query.send_keys('686384')
searchbar_query.click()

articles = driver.find_element(By.CLASS_NAME,"articles")
articles_list = articles.find_element(By.CLASS_NAME,"articles-result")
description = articles_list.find_element(By.CLASS_NAME,"truncate")

print(description.text)
