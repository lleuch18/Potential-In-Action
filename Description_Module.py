# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 13:35:13 2024

@author: Lasse
"""
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



# VARIABLES ONLY FOR TEST ENVIRONMENT
page_url = "https://www.cenger.dk/varekatalog/3dfusion-wedge-100-stk-large-groen"



def Locate_Description(page_url,Product_Page):    
    content = Product_Page.find_element(By.ID,"content1")

    
    description = content.find_element(By.ID,"description")
    
    return description.text

# Retrieve Webpage
def Simulate_Page(page_url):
    # TODO: Change Selenium to pure requests module
    """
    Function to open the chrome simulation in Selenium
    

    Parameters
    ----------
    page_url : URL of the webpage to be accessed

    Returns
    -------
    The webpage containing the product text for scraping
    """
    
    options = webdriver.ChromeOptions()
    options.add_argument("–headless")    
    options.add_argument("–disable-extensions")
    driver = webdriver.Chrome()
    
    
    Product_Page = driver.get(page_url)
    
    text = Locate_Description(page_url,Product_Page)
    
    print(text)
    
    
Simulate_Page(page_url)
    
# CENGER

    
    


    