from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {"executable_path": "/usr/local/bin/chromedriver"}
    return Browser("chrome", **executable_path, headless=False)

#create dictionary to append mars scraping info for mongodb
mars_db = {}

#scrape NASA MARS NEWS 
def scrape_nasa_mars_news():
    try:
        browser= init_browser()
        
        url = 'https://mars.nasa.gov/news/'
        browser.visit(url)   
        html = browser.html
        soup = bs(html, 'html.parser')


       # Identify and return title of article
        news_title = soup.find('div', class_="content_title").find('a').text
        # Identify and return description paragraph 
        news_p = soup.find('div', class_="article_teaser_body").text

        #create dictionary entry for mars news info
        mars_db['news_title'] = news_title
        mars_db['news_paragraph'] = news_p

        
        return mars_db

    finally:

        browser.quit()
        
#scrape NASA MARS NEWS 
def scrape_JPL_space_images():
    try:
        browser= init_browser()
        
        image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url)
        html_img = browser.html
        soup = bs(html_img, 'html.parser')

        #results = soup.find_all('li', class_="slide")
    
    # Iterate through each image
    
        featured_image = image_soup.find_all('a', class_="fancybox")[1]
        img_link = featured_image["data-thumbnail"]
        #print(img_link)
        main_url = 'https://www.jpl.nasa.gov'
        featured_image_url = main_url + img_link
        print(featured_image_url)
            

        #create dictionary entry for mars news info
        mars_db['featured_image_url'] = featured_image_url

        
        return mars_db

    finally:

        browser.quit()
