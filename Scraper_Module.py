# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 11:08:55 2024

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

from selenium.common.exceptions import NoSuchElementException

import pandas as pd




#%% Basiq Scraper
def basiq_scraper(driver,artikel_nr):
    time.sleep(4)

    try:
        cookies_button = driver.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
        cookies_button.click()
    except NameError:
        print("No Cookies Window")


    searchbar = driver.find_element(By.CLASS_NAME,"searchbox")
    searchbar.send_keys(artikel_nr)
    searchbar.send_keys(Keys.ENTER)

    bd = driver.find_element(By.CLASS_NAME,"bd")
    bd.size
    bd_content = bd.find_element(By.CLASS_NAME,"m2d-body-content");bd_content.size
    #search_results = bd_content.find_element(By.XPATH,"//cx-page-layout[@class='SearchResultsListPageTemplate ng-star-inserted']")
    search_results = bd_content.find_element(By.XPATH,"//cx-page-layout")
    search_result_list = search_results.find_element(By.XPATH,"//cx-page-slot[@position='SearchResultsListSlot']")
    
    product = search_results.find_element(By.XPATH,"//m2d-product-list-item[@class='cx-product-search-list ng-star-inserted']")
    product.size
    product.click()

    description = driver.find_element(By.TAG_NAME,"h1")

    driver.close()
    
    return description.text

#%% Cliniclands Scraper
def cliniclands_description_scraper(driver,artikel_nr):    
    
    
    try:
        shadow_host = driver.find_element(By.ID, "usercentrics-root"); shadow_host.size
        shadow_root = driver.execute_script('return arguments[0].shadowRoot', shadow_host)
        cookies_button = shadow_root.find_element(By.CSS_SELECTOR, '[data-testid=uc-accept-all-button]')
        cookies_button.click()
    except NoSuchElementException:
        pass
    
    page_content = driver.find_element(By.ID,"wrapper")
    searchbar_box = page_content.find_element(By.ID,"search")
    searchbar = searchbar_box.find_element(By.CLASS_NAME,"searchbar")
    searchbar_form = searchbar_box.find_element(By.CLASS_NAME,"form")
    searchbar_query = searchbar_form.find_element(By.CLASS_NAME,"query")
    
    searchbar_query.send_keys(artikel_nr)
    searchbar_query.click()
    
    time.sleep(3)
    
    articles = driver.find_element(By.CLASS_NAME,"articles")
    articles_list = articles.find_element(By.CLASS_NAME,"articles-result")
    description = articles_list.find_element(By.XPATH,"//tbody[1]/tr[1]/td[@class='name']/div/span/a")
   # description = description_path.find_element(By.CLASS_NAME,"truncate")
    
    return description.text
#%% Plandent Scraper
def plandent_description_scraper(driver,artikel_nr):
    
    # Setup wait for later
    wait = WebDriverWait(driver, 10)

    #Save Original Tab Handle
    original_window = driver.current_window_handle
    
    #Accept Cookies
    try:
        cookie_menu = driver.find_element(By.CLASS_NAME,"coi-button-group")
        accept_button = cookie_menu.find_element(By.CLASS_NAME,"coi-banner__accept")
        accept_button.click()
    except NameError:
        print("No Cookies Menu")
    
    #Find Searchbar
    searchbar = driver.find_element(By.CLASS_NAME,"header__search").find_element(By.XPATH,"//div[@class='search-bar']")
    
    #Switch Search from Articles to Products
    #Locate and click on dropdown menu
    searchbar_dropdown = searchbar.find_element(By.XPATH,"div[@class='search-bar__dropdown dropdown']")
    searchbar_dropdown.click()
    searchbar_dropdown_show = searchbar.find_element(By.XPATH,"div[@class='search-bar__dropdown dropdown show']")
    #Select Articles
    searchbar_articles_button = searchbar_dropdown_show.find_element(By.XPATH, "div[@class='search-bar__dropdown-menu dropdown-menu']").find_element(By.XPATH,"//a[contains(text(),\'Produkter')]")  
    searchbar_articles_button.click()
    
    #Input Article nr. to search form
    searchbar_input = driver.find_element(By.CLASS_NAME,"search-bar__input")
    searchbar_input.send_keys('19504')
    searchbar_button = searchbar_input.find_element(By.XPATH,"//button[@class='search-bar__submit']")
    
    searchbar_button.click()
    
    #Wait for new window to open
    wait.until(EC.number_of_windows_to_be(2))
    
    #Loop thorugh window handles in driver untill one new window is reached
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break
    
    
    
    #Remove Popup if present
    try:
        #Site contains nested shadowroots NOTE: ShadowDOM doesn't support xpath
        #Locate 1st Shadowhost
        shadow_host_1st = wait.until(EC.presence_of_element_located((By.XPATH,"//*[starts-with(name(),'sleeknote-') and contains(name(),'top')]")))
        #shadow_host_1st = driver.find_element(By.XPATH,"//*[starts-with(name(),'sleeknote-') and contains(name(),'top')]")
        #Locate 1st shadowroot
        shadow_root_1st = driver.execute_script('return arguments[0].shadowRoot', shadow_host_1st)       
        #Locate 2nd shadowhost and 2nd shadowroot
        shadow_host_2nd =  shadow_root_1st.find_element(By.CSS_SELECTOR, "sleeknote-form")
        shadow_root_2nd = driver.execute_script('return arguments[0].shadowRoot', shadow_host_2nd)
        
        #Locate popup close button and click
        popup_close_button = wait.until(EC.element_to_be_clickable(shadow_root_2nd.find_element(By.CSS_SELECTOR,"#sleeknote-Step--1 > form > ul > li:nth-child(2) > div")))
        #Despite Explicit wait still click not synchronized
        time.sleep(1)
        popup_close_button.click()
    except NameError:
        print("Popup not detected")
        
    #Find Description
    #Note: FULL XPATH FOR main_container
    try:
        main_container = driver.find_element(By.XPATH,"/html/body/form[2]/div[4]")
    except NameError:
        print("main_container not found. Consider switching from FULL XPATH")
        
    content_container = main_container.find_element(By.XPATH,"//*[@id='ContentContainer']");content_container.size
    content = content_container.find_element(By.XPATH,"//*[@id='Content']");content.size
    onkeypress = content.find_element(By.XPATH,'//*[@id="Content"]/div[2]/div[3]')
    
    description = onkeypress.find_element(By.XPATH,'//*[@id="ctl00_ContentPlaceHolder1_repAllBrandProductList_ctl01_ctlProduct_hypProductName"]')
    
    driver.close()
    
    return description
    
    
    
    
#%% Cenger Scraper
def cenger_description_scraper(driver,artikel_nr,login=False,user_id=None,password=None):
    """
    

    Parameters
    ----------
    driver : WebdriverElement with mainpage loaded
    artikel_nr : Article nr. to be tested.
    login : Login functionality implemented for price description. The default is False.
    user_id :  The default is None.
    password : The default is None.

    Returns
    -------
    product description.

    """


    if login == True:
        #Locate log_in button in row
        #[1]cengerContainer/[DesktopSection/Content1/section productView/container customContainer/row/col-md-12/row/col-md-6/cold-md-12-loginForPrices
        login_button = driver.find_element(By.XPATH,"html[1]/body[1]/div[1]/div[2]/div[3]/div[2]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[1]")
    
        #Locate login button element (Cookies need to be handled)
        login_button.size
        login_button.location
        login_button.click()
    
        #Locate the login_menu element
        login_menu = driver.find_element(By.CLASS_NAME,"form")
        login_menu.location
        login_menu.size
        #Locate the username label
        id_label = login_menu.find_element(By.NAME,"Username")
        id_label.size
        #Locate the password label
        password_label = login_menu.find_element(By.NAME,"Password")
        password_label.size
    
        #Send login credentials
        id_label.send_keys(user_id)
        password_label.send_keys(password)

        #Locate login button within login form
        column = driver.find_element(By.NAME,"ExtUserForm")
        
        #//Tagname[@AttibuteName = ‘value’]
        #login_menu_button = column.find_elements(By.XPATH,'//form[contains(text(),"Log ind")]')#//ExtUserForm[@class="button"');
        column.length
        #login_menu_button = column.find_elements(By.XPATH,'.//form[@Class="button"]')
        login_menu_button = column.find_element(By.CLASS_NAME,'button'); login_menu_button.size
        login_menu_button.click()
        
    #Locate description independent of login    
    menuBar = driver.find_element(By.CLASS_NAME, "menuBar");menuBar.size
    
    container = menuBar.find_element(By.CLASS_NAME, "container"); container.size
    
    row  = container.find_element(By.CLASS_NAME, "row"); row.size
    
    searchbar = row.find_element(By.ID, "instantSearch");searchbar.size
    searchbar.send_keys(artikel_nr)
    searchbar.send_keys(Keys.ENTER)
    
    product_desktopSection = driver.find_element(By.CLASS_NAME,"desktopSection");product_desktopSection.size
    product_description = product_desktopSection.find_element(By.CLASS_NAME,'description')
    description = product_description.find_element(By.TAG_NAME,"b")
        

    # cont = input("Close Chrome Session [Y/N]").upper()
    # if cont == "Y":
    #     #closing the driver
    #     driver.close()

    # dm.Locate_Description(page_url)
    
    
    
    return description.text