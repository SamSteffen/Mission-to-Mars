# Mission-to-Mars

### Project Outline
This analysis demonstrates the creation of a portfolio of data collected via webscraping using Splinter, BeautifulSoup, MongoDB, Flask and Bootstrap.

- Using Python, we wrote a script to pull the latest article from the website, https://redplanetscience.com, searching by html tags.
- Using a similar method, we pulled the most recent image of mars posted from a second website, https://spaceimages-mars.com, and generated an absolute url for the results of the search.
- From a third website, https://galaxyfacts-mars.com, we pulled data from a table comparing facts about Earth and Mars. We converted this data to a pandas dataframe using pandas, then converted it back to html.

After completing the above script, we initialized a mars_app database using MongoDB to store our data.

We then wrote a Python script that uses Flask dependencies to tie our web-scraped html to a MongoDB database and print the output on a shareable webpage. Prior to running this, we refactored our intial scraping code to translate our Python actions into functions for greater reusability. 

Once the results of our webscraping functions were saved, we used Bootstrap to change the formatting and provide a cleaner presentation of the results. We then further modified our webpage by adding additional full-size images of Mars.

# Summary
To retrieve these images, we added a script to our previous Python code to visit another webpage, https://marshemispheres.com/, which contains links to seperate webpages with full-size images and urls. Using a for loop, we scraped the full-size image urls and the image titles into a dictionary, and then placed the dictionaries into an iterable list. 

We then refactored the above code to create a function, which was added to our scraping.py file. To make sure the code was working properly we activated Mongo and were able to see the data in our Mongo database:

[mongo image]

# Results
We further modified our webpage html to include bootstrap features to accommodate the new images, including:
- .img-thumbnail class, which shapes our very large images into thumbnails.
- class="mx-auto d-block" which keeps the image centered.
- class="jumbotron jumbotron-fluid" which adjusts the size of the jumbotron to accommodate different screen sizes.
