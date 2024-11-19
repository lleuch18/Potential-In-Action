# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 13:20:37 2024

@author: Lasse
"""

import streamlit as st
import pandas as pd
import numpy as np
import snowflake.connector
import streamlit_option_menu
from streamlit_option_menu import option_menu



import os 

import time
import random

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
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
import GUI_Run_Tests as test
reload(test)


with st.sidebar:
    
    options = st.selectbox("Select Competitor", ('Basiq','Cenger','Cliniclands','Plandent'))
    
    test_meta_data = st.text_input("Name of test")
    
    article_start = st.number_input("Begin at article:",step=1,value=None)
    
    article_end = st.number_input("End at article:",step=1,value=None)    
   
    
    selected = option_menu(
    menu_title = "Main Menu",
    options = ['Set test parameters','Perform Test'],
    icons = ["gear-wide-connected","gem"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
)


    
   
if selected == "Perform Test":
    st.header('Nordscraper')
    # Create a row layout
    c1, c2= st.columns(2)
    c3, c4= st.columns(2)

    with st.container():
        c1.write("c1")
        #st.button("Plain_button")
        # c2.write("c2")

    # with st.container():
        # c3.write("c3")
        # c4.write("c4")

    with c1:
        varenr,beskrivelse,page_url, data, artikel_numre, artikel_descriptions = test.comptetitor_variables(options)
            
        table_data = pd.DataFrame.from_dict([{varenr: "start", beskrivelse: "start             "}])
        
        #column_config=st.column_config.Column(label=None, width="large", help=None, disabled=None, required=None)  
        display_table = st.dataframe(table_data                                     )
    
    cnt = 0    
    for artikel in range(article_start,article_end+1):  
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)  
        
        driver.get(page_url)
        
        cnt = cnt+1
        
        description,artikel_nr = test.run_tests(data,driver,options,artikel_numre,artikel)
        
        display_table.add_rows(pd.DataFrame.from_dict([{varenr: str(artikel_nr), beskrivelse: str(description)}])) 
        
        
        driver.close()
        
        time.sleep(random.randrange(20,35))
        



