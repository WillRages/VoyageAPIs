from flask import Flask, render_template, request
import requests
from forms import hotelForm
import json
import sqlalchemy

app = Flask(__name__)
app.config["SECRET_KEY"] = "csgod"

global hotelJSONdata

@app.route("/")
def homePage():
    return "Home"


@app.route("/hotel")
def HotelPage():
    form = hotelForm()
    return render_template("hotelform.html", form=form)

@app.route("/hotelout",methods=["GET","POST"])
def HotelOutput():

    if request.values.get("getHotels") == "y":

        location = request.values.get("getPlace")

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
        
        response = responseForHotel.json()  # Do stuff with this data
        hotels = []
        for hotel in response["suggestions"][1]["entities"]:
            hotels.append(hotel["name"])

        hotelJSONdata = hotels

        
        
        with open("hotelData.json", "w+") as f:
           f.write(responseForHotel.text) #make sure you write to the file
    else:
        hotelJSONdata = "no checkbox"
    return render_template("hotelOutput.html", Hotels = hotelJSONdata)

app.run(host="0.0.0.0")