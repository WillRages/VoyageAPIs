from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, StringField

class hotelForm(FlaskForm):
  getHotels = BooleanField("Hotels Near Me")
  getPlace = StringField("Where do you want to go?")
  submit = SubmitField("Submit")