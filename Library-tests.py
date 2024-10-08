# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import requests
from bs4 import BeautifulSoup


#url = 'https://www.basiqdental.dk/da_DK/p/profylakse/tandbeskyttelse/fluor/clinpro-clear-fluoride-treatment-50pcs-l-pop-doses-mint/498461' 
url = 'https://www.geeksforgeeks.org/python-programming-language/'


#%% Standard Test 

# Making a GET request
r = requests.get(url)
# check status code for response received
# success code - 200
print(r)

# print content of request
print(r.content)

#%% Test BeautifulSoup

# Making a GET request
r = requests.get(url)

# check status code for response received
# success code - 200
print(r)

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())

#%% Extract Data from nested HTML structure

s = soup.find('div', class_='entry-content')
content = s.find_all('p')

print(content)

