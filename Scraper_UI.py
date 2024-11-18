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

import GUI_Run_Tests as test

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


with st.sidebar:
    
    options = st.selectbox("Select Competitor", ('Basiq','Cenger','Cliniclands','Plandent'))
    
    test_meta_data = st.text_input("Name of test")
    
    article_start = st.number_input("Begin at article:",step=1,value=None)
    
    article_end = st.number_input("End at article:",step=1,value=None)
    
    
    
    selected = option_menu(
    menu_title = "Main Menu",
    options = ['Perform Test','Perform Data Collection'],
    icons = ["gem","gear-wide-connected"],
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
        # c2.write("c2")

    # with st.container():
        # c3.write("c3")
        # c4.write("c4")

    with c1:
        match options:
            case "Basiq":
                varenr = 'Basiq Varenummer'
                beskrivelse = 'Basiq Beskrivelse'                
            case "Cenger":
                varenr = 'Cenger Varenummer'
                beskrivelse = 'Cenger Beskrivelse'                
            case "Cliniclands":
                varenr = 'Cliniclands Varenummer'
                beskrivelse = 'Cliniclands Beskrivelse'                
            case "Plandent":
                varenr = 'Plandent Varenummer'
                beskrivelse = 'Plandent Beskrivelse'
                
        table_data = pd.DataFrame(columns=[varenr,beskrivelse])
        st.dataframe(table_data)
    
    cnt = 0    
    for artikel in range(article_start,article_end+1):  
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)  
        
        driver.get(page_url)
        
        cnt = cnt+1
        
        description,article = test.run_tests(article_start,article_end,competitor=options,test_meta_data=test_meta_data)
        
        table_data.add_rows(pd.DataFrame({varenr: article, beskrivelse: description})) 
        
        
           
    # with c2:
    #     chart_data = pd.DataFrame(np.random.randn(20, 3),columns=["a", "b", "c"])
    #     st.bar_chart(chart_data)

    # with c3:
    #     chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    #     st.line_chart(chart_data)

    # with c4:
    #     chart_data = pd.DataFrame(np.random.randn(20, 3),columns=['a', 'b', 'c'])
    #     st.line_chart(chart_data)
        
    
# if selected == "Warehouse":
#     st.subheader(f"**You Have selected {selected}**")
#     my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
#     my_cur = my_cnx.cursor()
#     # run a snowflake query and put it all in a var called my_catalog
#     my_cur.execute("select * from SWEATSUITS")
#     my_catalog = my_cur.fetchall()
#     st.dataframe(my_catalog)
#     q1 = st.text_input('Write your query','')
#     st.button('Run Query')
#     if not q1:
#       st.error('Please write a query')
#     else:
#       my_cur.execute(q1)
#       my_catalog = my_cur.fetchall()
#       st.dataframe(my_catalog)

    
if selected == "Contact":
    st.subheader(f"**You Have selected {selected}**")
    
