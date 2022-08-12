# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

# ### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')

slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url

# ### Mars Facts

df = pd.read_html('https://galaxyfacts-mars.com')[0]

df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)

df.to_html()

# # D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles
# ### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

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
    browser.visit(f'https://marshemispheres.com/{h_ref}')
    
    #parse the html on the new page
    html2 = browser.html
    img_soup = soup(html2, 'html.parser')
    
    #find the title and set it to a variable
    title = img_soup.find("h2", class_="title").text
        
    #retrieve the url and set it to a variable
    partial_url = img_soup.find('img', class_='wide-image').get('src')
    url = f'https://spaceimages-mars.com/{partial_url}'
    
    #add the scraped title and url variables to the dictionary
    hemispheres['title'] = title
    hemispheres['url'] = url
        
    #add the dictionary to 
    hemisphere_image_urls.append(hemispheres)
       
    #navigate back to the main page
    browser.back()

# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls

# 5. Quit the browser
browser.quit()