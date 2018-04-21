import random
import json
import requests
from flask import (Flask,
                   request,
                   url_for,
                   render_template)

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/data.json")
def data():
    # TODO read temperature and humidity from Arduino
    indoor_temp = random.randint(60,80)
    indoor_humidity = random.random()
    # TODO read temperature and humidity from openweathermap.org
    payload = {'q': 'Annapolis','units':'imperial','APPID':'631ff851f1ece3754797d45cd9573bb0'}
    r = requests.get('http://api.openweathermap.org/data/2.5/weather', params=payload)
    r.json()
    r.dict = json.loads(r.text)
    outdoor_temp = r.dict['main']['temp']
    outdoor_humidity = r.dict['main']['humidity']
    return json.dumps({
        "indoor_temp": indoor_temp,
        "indoor_humidity": indoor_humidity,
        "outdoor_temp": outdoor_temp,
        "outdoor_humidity": outdoor_humidity})


@app.route("/cheep",methods=['POST'])
def cheep():
    name = request.form['name']
    message = request.form['message']
    print("got a cheep from [%s]: %s" % (name,message))
    # TODO: append [name: message] to a file of cheeps
    # TODO: display the cheep on the kit LCD
    return render_template('thankyou.html')
