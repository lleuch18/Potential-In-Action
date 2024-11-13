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
#%% TEMP Define Functions in Script
def cenger_find_description(driver,artikel_nr):
    menuBar = driver.find_element(By.CLASS_NAME, "menuBar");menuBar.size
    
    container = menuBar.find_element(By.CLASS_NAME, "container"); container.size
    
    row  = container.find_element(By.CLASS_NAME, "row"); row.size
    
    searchbar = row.find_element(By.ID, "instantSearch");searchbar.size
    searchbar.send_keys(artikel_nr)
    searchbar.send_keys(Keys.ENTER)
    
    product_desktopSection = driver.find_element(By.CLASS_NAME,"desktopSection");product_desktopSection.size
    product_description = product_desktopSection.find_element(By.CLASS_NAME,'description')
    specific_text = product_description.find_element(By.TAG_NAME,"b")
    
    #print(specific_text.text)
    
    
    return specific_text.text
#%% Testing Accuracy of Description Retrieval
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

#page_url = "https://www.cenger.dk/varekatalog/3dfusion-wedge-100-stk-large-groen"

page_url = "https://www.cenger.dk/"
data = pd.read_excel("C:/Users/Lasse/OneDrive/Skrivebord/Potential-In-Action/Web-Scraping/Data Cenger.xlsx")
artikel_numre = data["Cenger varenr."]
artikel_descriptions = data["Cenger beskrivelse"]

artikel_start = 4
artikel_end = 5

test_meta_data = input("input test number")
test_meta_data = f"Test nr. {test_meta_data} \narticle_start = {artikel_start} \narticle_end = {artikel_end}"

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
#driver.get(page_url)

test_success = {}

cnt = 0

for artikel in range(artikel_start,artikel_end+1):
    driver.get(page_url)
    
    cnt = cnt+1
    
    artikel_nr = artikel_numre[artikel]
    
    description = cenger_find_description(driver,artikel_nr)
    
    print(f"At loop {cnt} for artikel {artikel_nr} description: \n {description}")
    
    
    #housekeep
    if description == artikel_descriptions[artikel]:
        test_success[artikel] = 1
    else:
        test_success[artikel] = 0
        
    
        
    time.sleep(random.randrange(20,35))
        
with open('Cenger.txt', 'w') as file:
    file.write(test_meta_data)
    
    file.write(repr(test_success) + "\n\n\n")

test_success

print("test concluded")







#%% Section used for retrieving complete description of product
# product_row = driver.find_element(By.ID, "content1");product_row.size 

# product_container = product_row.find_element(By.CLASS_NAME, "productsContainer");product_container.size

# product_gridrow = product_container.find_element(By.CLASS_NAME,"gridRow")
# product_tableRow = product_gridrow.find_element(By.CLASS_NAME,"tableRow")
# product_tableRow.click()

# driver.find_element(By.CLASS_NAME,"container customContainer")
# #product_description = product_row.find_element(By.CLASS_NAME,"description");product_description.size
# #specific_text = product_description.find_element(By.TAG_NAME,"b")

# #print(product_description.text)
# #content = driver.find_element(By.ID,"content1")


# #description = content.find_element(By.CLASS_NAME,"description")

# #print(description.text)