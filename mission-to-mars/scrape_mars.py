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

        results = soup.find_all('li', class_="slide")
        images = []
    # Iterate through each image
        for result in results: 
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
            try:
                featured_image = result.find('a', class_="fancybox").text
        # Identify and return link to listing
                title = result.a["data-title"]
                link = result.a['data-fancybox-href']
            

        # Print results only if title and link are available
                if (title and link):
                    print('-------------')
                    print(f"image title = {title}")
                    print(f"featured_image_url = https://www.jpl.nasa.gov{link}")
                    images.append(title)
                    images.append(link)
            
            except AttributeError as e:
            print(e)
            
                          partial_url= images[11]
                          main_url = 'https://www.jpl.nasa.gov'
                          featured_image_url = main_url + partial_url

        #create dictionary entry for mars news info
                                mars_db['featured_image_url'] = featured_image_url

        
           return mars_db

    finally:

        browser.quit()
        
#scrape NASA MARS NEWS 
def scrape_mars_weather():
    try:
        browser= init_browser()
        
        weather_url = 'https://twitter.com/marswxreport?lang=en'
        browser.visit(weather_url)
        html_weather = browser.html
        soup = bs(html_weather, 'html.parser')

        
        results = soup.find_all('div', class_="js-tweet-text-container")
        tweets = []
    # Iterate through each book
               for result in results: 
        # Use Beautiful Soup's find() method to navigate and retrieve attributes
                    try:
                        latest_tweet = result.find('p', class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
        # Print results only if title, price, and link are available
                       if (latest_tweet):
                            print('-------------')
                            print(f"mars_weather = {latest_tweet}")
                            tweets.append(latest_tweet)
            
                    except AttributeError as e:
                    print(e)
                        
                        mars_weather = tweets[0]

        #create dictionary entry for mars news info
                            mars_db['mars_weather'] = mars_weather

        
          return mars_db

    finally:

        browser.quit()
 
        
#scrape Mars facts
def scrape_mars_facts():
    try:
        
           url = 'https://space-facts.com/mars/' 
               tr = pd.read_html(url)
                
                mars_facts_df = tr[1]

                mars_facts_df.columns = ['Description','Value']

                mars_facts_df.set_index('Description', inplace=True)
                
                html_table = mars_facts_df.to_html()
                
                html_table.replace('\n', '')
                
                mars_facts = mars_facts_df.to_html()
                
                     mars_db['mars_facts'] = facts

        
        return mars_db
    
    finally:
        browser.quit()
        
#scrape mars hemispheres 
        
def scrape_mars_hemispheres():
    try:
        
        hemisphere_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
         browser.visit(hemisphere_url)
             html_hemisphere = browser.html

                  soup = bs(html_hemisphere, 'html.parser')
        
        
                       results = soup.find_all('div', class_='item')
                       hemisphere_image_urls = []

                       hemisphere_main_url = 'https://astrogeology.usgs.gov'

                       for result in results: 
    
                            title = result.find('h3').text
                            partial_image_url = result.find('a', class_='itemLink product-item')['href']
        
                            browser.visit(hemisphere_main_url + partial_image_url)
    
                            partial_image_html = browser.html
    
                            soup = bs(partial_image_html, 'html.parser')
    
                            img_url = hemisphere_main_url + soup.find('img', class_='wide-image')['src']
    
                            hemisphere_image_urls.append({"title" : title, "img_url" : img_url})
        
                                mars_db['hemisphere_image_urls'] = hemisphere_image_urls
        
                return mars_db
    
    finally:
        browser.quit()
        
        
        
        

        

        
        
        
        
        
        
