from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
from splinter import Browser
#import time 

def init_browser():
    # @NOTE: Replace the path with your actual path to the chromedriver
    executable_path = {'executable_path': '/Users/sofiahorenstein/Downloads/chromedriver 3'}
    browser = Browser('chrome', **executable_path, headless=False)

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
    except:
        pass
   
        
#scrape NASA MARS NEWS 
def scrape_JPL_space_images():
    try:
        browser= init_browser()
        
        image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
        browser.visit(image_url)
        html_img = browser.html
        image_soup = bs(html_img, 'html.parser')

        #results = soup.find_all('li', class_="slide")
    
    # Iterate through each image
    
        featured_image = image_soup.find_all('a', class_="fancybox")[1]
        img_link = featured_image["data-thumbnail"]
        #print(img_link)
        main_url = 'https://www.jpl.nasa.gov'
        featured_image_url = main_url + img_link
        #print(featured_image_url)
             

        #create dictionary entry for mars news info
        mars_db['featured_image_url'] = featured_image_url

        
        return mars_db
    except:
        pass
    
        
#scrape NASA MARS NEWS 
def scrape_mars_weather():
    try:
        browser= init_browser()
        
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)
        html_weather = browser.html
        weather_soup = bs(html_weather, 'html.parser')

        mars_weather = weather_soup.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").get_text()
        #print(f"mars_weather = {mars_weather}")

        mars_db['mars_weather'] = mars_weather

        
        return mars_db
    except:
        pass
   
        
#scrape Mars facts
def scrape_mars_facts():
    try:
        
        mars_facts_url = 'https://space-facts.com/mars/' 

        mars_facts = pd.read_html(mars_facts_url)
                
        mars_facts_df = mars_facts[1]

        mars_facts_df.columns = ['Description','Value']

        mars_facts_df.set_index('Description', inplace=True)
                
        mars_facts_data = mars_facts_df.to_html()
                
        mars_db['mars_facts'] = mars_facts_data
        
        return mars_db
    except:
        pass
    
#scrape mars hemispheres 
#def scrape_mars_hemispheres():
        
    #hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    #browser.visit(hemisphere_url)
    #html_hemisphere = browser.html
    #soup = bs(html_hemisphere, 'html.parser')
        
    #results = soup.find_all('div', class_='item')
    #hemisphere_image_urls = []

    #hemisphere_main_url = 'https://astrogeology.usgs.gov'

    #for result in results: 

        #title = result.find('h3').text
        #partial_image_url = result.find('a', class_='itemLink product-item')['href']
    
        #browser.visit(hemisphere_main_url + partial_image_url)

        #partial_image_html = browser.html

        #soup = bs(partial_image_html, 'html.parser')

        #img_url = hemisphere_main_url + soup.find('img', class_='wide-image')['src']

        #hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
    
        #mars_db['hemisphere_image_urls'] = hemisphere_image_urls
    
    return mars_db
