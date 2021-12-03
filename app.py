from flask import Flask, render_template, request ,url_for
import ssl
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut
import joblib as jb
import numpy as np
import json


app = Flask(__name__)

model = jb.load("model.joblib")
ssl._create_default_https_context = ssl._create_unverified_context

def target_encoding(result):
    dic = {1: 'Operating',
           2: 'Acquired', 
           3: 'Closed',
           4: 'IPO'}
    return dic[result]

def get_status(input_json):
    data = len(input_json)

    x = np.zeros(data)
    x[0] = input_json['founding_year']
    x[1] = input_json['funding_rounds']
    x[2] = input_json['funding_amount']
    x[3] = input_json['milestones']
    x[4] = input_json['relationship']
    x[5] = input_json['lat']
    x[6] = input_json['long']
    
    x_shaped = x.reshape(1, -1)

    result = int(model.predict([x]))

    return result

@app.route('/')

def index():
    return render_template('index.html') 

@app.route('/predict',methods=['POST'])

def predict():

    if request.method == 'POST':

        geolocator = Nominatim(user_agent='user_agent')
        location = geolocator.geocode(request.form['ilocation'])

        input_json = {
            "founding_year": request.form['iyear'],
            "funding_rounds": request.form['ifrd'],
            "funding_amount": request.form['ifra'],
            "milestones": request.form['imil'],
            "relationship": request.form['irel'],
            "lat": location.latitude,
            "long": location.longitude
        }
        result = get_status(input_json)
        status = target_encoding(result)
        
    return render_template('predict.html',status=status)

if __name__=='__main__':
    app.run(debug=True)