# Mission-to-Mars
### Project Outline
This analysis demonstrates the creation of a portfolio of data collected via webscraping using Splinter, BeautifulSoup, MongoDB, Flask and Bootstrap.

- From the website, https://redplanetscience.com, we wrote a code to pull the latest articles posted by their html tags.
- From a second website, https://spaceimages-mars.com, we pulled images of the most recently posted image of mars, and generated an absolute url for the results of the search using a Python script.
- From a third website, https://galaxyfacts-mars.com, we pulled the data off of a table comparing facts about Earth and Mars. We converted this data to a pandas dataframe using pandas, then converted it back to html.

Following this we initialized a mars_app database using MongoDB to store our data.

We then wrote a Python script that uses Flask dependencies to tie our web-scraped html to a MongoDB database and print the output on a shareable webpage. Prior to running this, we refactored our intial scraping code to translate our Python actions into functions for greater reusability. 

Once the results of our webscraping functions were saved onto a viewable Flask output, we used Bootstrap to change the formatting and provide a cleaner presentation of the results.

# Summary

# Results
