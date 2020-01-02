from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars2
# Create an instance of Flask
app = Flask(__name__)
# Use PyMongo to establish Mongo connection
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

# Route to render index.html template using data from Mongo
@app.route("/")
def home():

    # Find one record of data from the mongo database
    mars_db = mongo.db.mars_db.find_one()

    # Return template and data
    return render_template("index.html", mars_db=mars_db)


# Route that will trigger the scrape function
@app.route("/scrape")
def scrape():
    mars_db_data = {}
    # Run the scrape function
    mars_db = mongo.db.mars_db
    mars_db_data['news'] = scrape_mars2.scrape_nasa_mars_news()
    mars_db_data['images'] = scrape_mars2.scrape_JPL_space_images()
    mars_db_data['weather'] = scrape_mars2.scrape_mars_weather()
    mars_db_data['facts'] = scrape_mars2.scrape_mars_facts()
    #mars_db_data = scrape_mars2.scrape_mars_hemispheres()
    print(mars_db_data)
    # Update the Mongo database using update and upsert=True
    mars_db.update({}, mars_db_data, upsert=True)
    # Redirect back to home page
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)