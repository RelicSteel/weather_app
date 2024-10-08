from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

# Loads the variables from .env - manly the API_KEY.
load_dotenv()

#This line Initialize's the Flask app
app = Flask(__name__)

API_KEY = os.getenv('API_KEY')
API_URL = "http://api.openweathermap.org/data/2.5/weather" # Basic weather call

# Setting up routes for homapage and weather search results

#route for the homepage
@app.route('/', methods=['GET', 'POST'])
def home():
    weather_data = None
    if request.method == 'POST':
        city = request.form.get('city')

        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }

        response = requests.get(API_URL, params=params)

        if response.status_code == 200:
            weather_data = response.json()

    return render_template('index.html', weather=weather_data)

if __name__ == '__main__':
    app.run(debug=True)