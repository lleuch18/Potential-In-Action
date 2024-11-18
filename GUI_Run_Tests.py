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


def run_tests(competitor,test_meta_data,article_start,article_end):

    
    
    
    test_success = {}
    
    
    
    
        
        
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
    
def comptetitor_variables(competitor):
    
    match competitor:
        case "Basiq":
            page_url = "https://www.basiqdental.dk/da_DK/"
            data = pd.read_excel("C:/users/lasse/onedrive/skrivebord/potential-in-action/web-scraping/Basiq Data set.xlsx")
            artikel_numre = data["Basiq varenr."]
            artikel_descriptions = data["Basiq beskrivelse"]
            
        case "Cenger":
             page_url = "https://www.cenger.dk/"         
             data = pd.read_excel("C:/Users/lasse/OneDrive/Skrivebord/potential-in-action/web-scraping/Data Cenger.xlsx")
             artikel_numre = data["Cenger varenr."]
             artikel_descriptions = data["Cenger beskrivelse"]
             
        case "Cliniclands":
            page_url = "https://www.cliniclands.dk/"
            data = pd.read_excel("C:/users/lasse/OneDrive/Skrivebord/potential-in-action/web-scraping/Data Cliniclands 24.10.2024.xlsx")
            artikel_numre = data["Cliniclands varenr."]
            artikel_descriptions = data["Cliniclands beskrivelse"]
            
        case "Plandent":
            page_url = "https://plandent.dk/"
            data = pd.read_excel("C:/users/lasse/OneDrive/Skrivebord/potential-in-action/web-scraping/Plandent.xlsx")
            artikel_numre = data["Plandent varenr."]
            artikel_descriptions = data["Plandent beskrivelse"]
        
    return page_url, data, artikel_numre, artikel_descriptions