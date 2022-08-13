#create a web app that ties web-scraped html to a Mongo database
from flask import Flask, render_template, redirect, url_for, request, abort
from flask_pymongo import PyMongo
import scraping

#set up Flask
app = Flask(__name__)

# use Flask_PyMongo to set up Mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mars_app"
mongo = PyMongo(app)

#define the route for the html page
@app.route("/")
def index():
   mars = mongo.db.mars.find_one()
   return render_template("index.html", mars=mars)

#define the route for the scraping route
@app.route("/scrape")
def scrape():
   mars = mongo.db.mars
   mars_data = scraping.scrape_all()
   mars.update_one({}, {"$set":mars_data}, upsert=True)
   return redirect('/', code=302)

#tell Flask to run the code
if __name__ == "__main__":
   app.run()