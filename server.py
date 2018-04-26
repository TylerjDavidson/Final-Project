import random
import json
import requests
import serial
from flask import (Flask,
                   request,
                   url_for,
                   render_template)

app = Flask(__name__)
s = serial.Serial("/dev/ttyACM0") #serial connection

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/data.json")
def data():
    s.write("p") #send cmd to send serial data from Arduino
    str_data = s.readline() #read data
    data = [int(x) for x in str_data.split(',')] #split data into two variables
    # TODO read temperature and humidity from Arduino
    #convert to Fahrenheit
    indoor_temp = round(data[0]*1.8+32)
    indoor_humidity = data[1]
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
    #print("got a cheep from [%s]: %s" % (name,message))
    with open("cheeps.log",'a') as f:
        f.write("%s: %s" %(name,message))
    # TODO: append [name: message] to a file of cheeps
    with open("cheeps.log",'a') as f:
        f.write("%s: %s" % (name,message))
    # TODO: display the cheep on the kit LCD

    s.write("l")
    msg = "%s: %s" % (name,message)

    s.write(msg.encode('utf-8'))
    return render_template('thankyou.html')
