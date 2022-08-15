# Import Splinter and BeautifulSoup
from distutils.log import error
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import datetime as dt

def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)
    #define news_title and news_paragraph variables
    news_title, news_paragraph = mars_news(browser)

    # Run all scraping functions and store results in dictionary
    data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now(),
      "hemispheres": hemisphere_data(browser)
    }

    # Stop webdriver and return data
    browser.quit()
    return data

#refactor code to make previous code a function
def mars_news(browser):
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)

    #set up the HTML parser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
    #add try/except for error handling
    try:
        slide_elem = news_soup.select_one('div.list_text')

        # locate the html webpage article title and summary text
        slide_elem.find('div', class_='content_title')

        # add the webpage article title and summary to a variable
        # Use the parent element to find the first `a` tag and save it as `news_title`
        news_title = slide_elem.find('div', class_='content_title').get_text()
    
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    
    except AttributeError:
        return None, None

    return news_title, news_p
 
# ## JPL Space Images Featured Image

#add function to refactor code
def featured_image(browser):
    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)

    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()

    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')

    try:
        # Find the relative image url
        img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
        return None

    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'

    return img_url

# ## Mars Facts

#add function to refactor code
def mars_facts():
    try:
        #use 'read_html' to scrape the facts from the table
        df = pd.read_html('https://galaxyfacts-mars.com')[0]
    except BaseException:
        return None
    
    df.columns=['description', 'Mars', 'Earth']
    df.set_index('description', inplace=True)
    
    return df.to_html()

#create a function to scrape the hemisphere data using code from Mission_to_Mars_Challenge.py
def hemisphere_data(browser):

    # 2. Create a list to hold the images and titles.
    hemisphere_image_urls = []
    
    #visit url
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    
    # 3. Write code to retrieve the image urls and titles for each hemisphere.
    #parse the webpage into html
    html = browser.html
    mars_soup = soup(html, 'html.parser')
    
    #REFERENCE: https://splinter.readthedocs.io/en/latest/elements-in-the-page.html
    #use the 'a' tags to navigate towards the clickable hrefs of the titular links
    a_tags = mars_soup.find_all('a', 'itemLink product-item')

    #add the hyperlink reference from each a_tag to a list using a for loop
    h_refs = []
    for each in a_tags[:8]:
        if each['href'] not in h_refs:
            h_refs.append(each['href'])
        else:
            continue
        
    # create a for loop to pass the hrefs into the url 
    for h_ref in h_refs:

        # create an empty dictionary, 'hemispheres'
        hemispheres = {}
    
        #generate a complete url using each href for each image and click it  
        browser.visit(f'https://astrogeology.usgs.gov/{h_ref}')
                
        #parse the html on the new page
        try:
            html2 = browser.html
            img_soup = soup(html2, 'html.parser')
        except NameError:
            return None

        try:
            #find the title and set it to a variable
            title = img_soup.find("h2", class_="title").text
        
        except AttributeError:
            return None
        
        try:
            #retrieve the url and set it to a variable
            url = img_soup.find_all('li')[0].a.get('href')
        
        except AttributeError:
            return None
           
        #add the scraped title and url variables to the dictionary
        hemispheres['title'] = title
        hemispheres['url'] = url
        
        #add the dictionary to the dictionary list
        hemisphere_image_urls.append(hemispheres)
       
        #navigate back to the main page
        browser.back()

    # 4. Print the list that holds the dictionary of each image url and title.
    return hemisphere_image_urls


if __name__ == "__main__":
    #if running as script, print scraped data
    print(scrape_all())

