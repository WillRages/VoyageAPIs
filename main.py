from flask import Flask, render_template, request
import requests
from forms import hotelForm
import json
import sqlite3
from sqlite3 import Error

app = Flask(__name__)
app.config["SECRET_KEY"] = "csgod"

global hotelJSONdata

@app.route("/")
def homePage():
    return "Home"


@app.route("/hotel")
def HotelPage():

    form = hotelForm()

    if request.args.get("getHotels") == "y":

        location = request.args.get("getPlace")

        urlforhotels = "https://hotels4.p.rapidapi.com/locations/v2/search"

        querystringforhotels = {
            "query": location,  # you change the place name to your liking which is nice
            "locale": "en_US",
            "currency": "USD",
        }

        headersforhotel = {
            "x-rapidapi-host": "hotels4.p.rapidapi.com",
            "x-rapidapi-key": "4b44744771mshe890455adb53acdp173a42jsned37231cf971",
        }

        responseForHotel = requests.get(
            urlforhotels, headers=headersforhotel, params=querystringforhotels
        )
        global hotelJSONdata
        hotelJSONdata = responseForHotel.json()  # Do stuff with this data

        with open("hotelData.json", "w+") as f:
           f.write(responseForHotel.text) #make sure you write to the file
    return render_template("hotelform.html", form=form)

@app.route("/hotelout")
def HotelOutput():
    global hotelJSONdata
    data = json.loads(hotelJSONdata)
    places = []
    for location in data["suggestions"][1]["entities"]:
        places.append(location["name"])
    return render_template("hotelOutput.html", Hotels = str(places))

app.run(host="0.0.0.0")