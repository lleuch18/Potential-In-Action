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
import pandas as pd

import time
import random


import Scraper_Module as sm
from importlib import reload
#Reload Scraper Module to implement code changes
reload(sm)

def run_tests(data,driver,competitor,artikel_numre,artikel):


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
        
  
    return description,artikel_nr
            
    
    
def comptetitor_variables(competitor):    
    
    
    match competitor:
        case "Basiq":
            page_url = "https://www.basiqdental.dk/da_DK/"
            #data = pd.read_excel("C:/users/lasse/onedrive/skrivebord/potential-in-action/potential-in-action/web-scraping/Data/Basiq Data set.xlsx")
            data = pd.read_excel("C:/Users/Lasse/OneDrive/Skrivebord/Potential-In-Action/Potential-In-Action/Data/Basiq Data set.xlsx")
            artikel_numre = data["Basiq varenr."]
            artikel_descriptions = data["Basiq beskrivelse"]
            varenr = 'Basiq Varenummer'
            beskrivelse = 'Basiq Beskrivelse'
            
        case "Cenger":
             page_url = "https://www.cenger.dk/"         
             #data = pd.read_excel("C:/Users/lasse/OneDrive/Skrivebord/potential-in-action/potential-in-action/web-scraping/Data Cenger.xlsx")
             data = pd.read_excel("C:/Users/Lasse/OneDrive/Skrivebord/Potential-In-Action/Potential-In-Action/Data/Data Cenger.xlsx")
             artikel_numre = data["Cenger varenr."]
             artikel_descriptions = data["Cenger beskrivelse"]
             varenr = 'Cenger Varenummer'
             beskrivelse = 'Cenger Beskrivelse'
             
        case "Cliniclands":
            page_url = "https://www.cliniclands.dk/"
            #data = pd.read_excel("C:/users/lasse/OneDrive/Skrivebord/potential-in-action/potential-in-action/web-scraping/Data Cliniclands 24.10.2024.xlsx")
            data = pd.read_excel("C:/Users/Lasse/OneDrive/Skrivebord/Potential-In-Action/Potential-In-Action/Data/Data Cliniclands 24.10.2024.xlsx")
            artikel_numre = data["Cliniclands varenr."]
            artikel_descriptions = data["Cliniclands beskrivelse"]
            varenr = 'Cliniclands Varenummer'
            beskrivelse = 'Cliniclands Beskrivelse'  
            
        case "Plandent":
            page_url = "https://plandent.dk/"
            #data = pd.read_excel("C:/users/lasse/OneDrive/Skrivebord/potential-in-action/potential-in-action/web-scraping/Plandent.xlsx")
            data = pd.read_excel("C:/Users/Lasse/OneDrive/Skrivebord/Potential-In-Action/Potential-In-Action/Data/Plandent.xlsx")
            artikel_numre = data["Plandent varenr."]
            artikel_descriptions = data["Plandent beskrivelse"]
            varenr = 'Plandent Varenummer'
            beskrivelse = 'Plandent Beskrivelse'
        
    return varenr,beskrivelse,page_url, data, artikel_numre, artikel_descriptions