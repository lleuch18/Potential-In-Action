""" # -*- coding: utf-8 -*-
"""

"""
import requests
from bs4 import BeautifulSoup


#url = 'https://www.basiqdental.dk/da_DK/p/profylakse/tandbeskyttelse/fluor/clinpro-clear-fluoride-treatment-50pcs-l-pop-doses-mint/498461' 
url = 'https://www.geeksforgeeks.org/python-programming-language-tutorial/'


#%% Standard Test 

# Making a GET request
r = requests.get(url)
# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

#%% Test BeautifulSoup
# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

#%% Extract Data from nested HTML structure

s = soup.find('div', class_='phrase__container')
content = s.find_all('p')

print(s)

#%% Selenium
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
# for holding the resultant list
element_list = []

for page in range(1, 3, 1):

    page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=" + str(page)
   # driver = webdriver.Chrome(ChromeDriverManager().install())
    driver = webdriver.Chrome()
    driver.get(page_url)
    title = driver.find_elements(By.CLASS_NAME, "title")
    price = driver.find_elements(By.CLASS_NAME, "price")
    description = driver.find_elements(By.CLASS_NAME, "description")
    rating = driver.find_elements(By.CLASS_NAME, "ratings")

    for i in range(len(title)):
        element_list.append([title[i].text, price[i].text, description[i].text, rating[i].text])

print(element_list)

#closing the driver
driver.close()

#%%% Modified Selenium Script (no loop, access scraped objects manually)
page_url = "https://webscraper.io/test-sites/e-commerce/static/computers/laptops?page=1"
# driver = webdriver.Chrome(ChromeDriverManager().install())
driver = webdriver.Chrome()
driver.get(page_url)
title = driver.find_elements(By.CLASS_NAME, "title")
price = driver.find_elements(By.CLASS_NAME, "price")
description = driver.find_elements(By.CLASS_NAME, "description")
rating = driver.find_elements(By.CLASS_NAME, "ratings")
title[0].click()


caption = driver.find_elements(By.CLASS_NAME,"caption")


#closing the driver
driver.close()

#region




#endregion """

import requests
from bs4 import BeautifulSoup
import sys
import time

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import os
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import pandas as pd

#page_url = "https://www.cenger.dk/varekatalog/3dfusion-wedge-100-stk-large-groen"

page_url = "https://www.cenger.dk/"
data = pd.read_excel(r"C:\Users\Lasse\OneDrive\Skrivebord\Potential-In-Action\Web-Scraping\Data Cenger.xlsx")
artikel_numre = data["Cenger varenr."]

artikel_nr = artikel_numre[1]

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get(page_url)




menuBar = driver.find_element(By.CLASS_NAME, "menuBar");menuBar.size

container = menuBar.find_element(By.CLASS_NAME, "container"); container.size

row  = container.find_element(By.CLASS_NAME, "row"); row.size

searchbar = row.find_element(By.ID, "instantSearch");searchbar.size
searchbar.send_keys(artikel_nr)
searchbar.send_keys(Keys.ENTER)

product_desktopSection = driver.find_element(By.CLASS_NAME,"desktopSection")
product_desktopSection.size

product_row = driver.find_element(By.ID, "content1");product_row.size 

product_container = product_row.find_element(By.CLASS_NAME, "productsContainer");product_container.size
product_gridrow = product_container.find_element(By.CLASS_NAME,"gridRow")
product_tableRow = product_gridrow.find_element(By.CLASS_NAME,"tableRow")
product_tableRow.click()

driver.find_element(By.CLASS_NAME,"container customContainer")
#product_description = product_row.find_element(By.CLASS_NAME,"description");product_description.size
#specific_text = product_description.find_element(By.TAG_NAME,"b")

#print(product_description.text)
#content = driver.find_element(By.ID,"content1")


#description = content.find_element(By.CLASS_NAME,"description")

#print(description.text)