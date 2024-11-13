# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 14:01:47 2024

@author: Lasse
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 10:49:17 2024

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

#Custom Module containing the Webscraping functions
import Scraper_Module as sm
from importlib import reload
#Reload Scraper Module to implement code changes
reload(sm)

def run_tests():
    
#Choose which competitor to test. Each competitor
    competitor = input("CHOOSE COMPETITOR\nBasiq: (B)\nCenger: (C)\nCliniclands: (CL)\nPlandent: (P)\n").upper()
    
    match competitor:
        case "B":
            page_url = "https://www.basiqdental.dk/da_DK/"
            data = pd.read_excel("C:/users/lasse/onedrive/skrivebord/potential-in-action/web-scraping/Basiq Data set.xlsx")
            artikel_numre = data["Basiq varenr."]
            artikel_descriptions = data["Basiq beskrivelse"]
            competitor = "Basiq"
        case "C":
             page_url = "https://www.cenger.dk/"         
             data = pd.read_excel("C:/Users/lasse/OneDrive/Skrivebord/potential-in-action/web-scraping/Data Cenger.xlsx")
             artikel_numre = data["Cenger varenr."]
             artikel_descriptions = data["Cenger beskrivelse"]
             competitor = "Cenger"
        case "CL":
            page_url = "https://www.cliniclands.dk/"
            data = pd.read_excel("C:/users/lasse/OneDrive/Skrivebord/potential-in-action/web-scraping/Data Cliniclands 24.10.2024.xlsx")
            artikel_numre = data["Cliniclands varenr."]
            artikel_descriptions = data["Cliniclands beskrivelse"]
            competitor = "Cliniclands"
        case "P":
            page_url = "https://plandent.dk/"
            data = pd.read_excel("C:/users/lasse/OneDrive/Skrivebord/potential-in-action/web-scraping/Plandent.xlsx")
            artikel_numre = data["Plandent varenr."]
            artikel_descriptions = data["Plandent beskrivelse"]
            competitor = "Plandent"
             
    
    
    artikel_start = int(input("Input article to begin testing at:"))
    artikel_end = int(input("Input article to end testing at:"))
    
    test_nr = input("Input test number")
    test_meta_data = f"Test nr. {test_nr} \narticle_start = {artikel_start} \narticle_end = {artikel_end}"
    
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=chrome_options)
    #driver.get(page_url)
    
    
    test_success = {}
    
    cnt = 0
    
    for artikel in range(artikel_start,artikel_end+1):
        driver.get(page_url)
        
        cnt = cnt+1
        
        #Python is 0 indexed and first row is column names, add 2 to compensate
        artikel_nr = artikel_numre[artikel+2]
        
        match competitor:        
            case "Basiq":
                description = sm.basiq_scraper(driver, artikel_nr)
            case "Cenger":
                description = sm.cenger_description_scraper(driver, artikel_nr)
            case "Cliniclands":
                description = sm.cliniclands_description_scraper(driver, artikel_nr)
            case "Plandent":            
                description = sm.plandent_description_scraper(driver, artikel_nr)
        
        print(f"At loop {cnt} for artikel {artikel_nr} description: \n {description}")
        
        
        #housekeep
        if description == artikel_descriptions[artikel]:
            test_success[artikel-2] = 1
        else:
            test_success[artikel-2] = 0
            
        
            
        time.sleep(random.randrange(20,35))
            
    with open(competitor+'.txt', 'w') as file:
        file.write(test_meta_data)
        
        file.write(repr(test_success) + "\n\n\n")
        
    print(f"Testing {test_nr} concluded")
    test_success