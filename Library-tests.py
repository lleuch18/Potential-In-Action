# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
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
