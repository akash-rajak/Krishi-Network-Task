
# impoted necessary library
import os
from flask import jsonify, request
import requests

# function defined to get the weather status
def getWeather():
    try:
        API_KEY = os.getenv("API_KEY") # here enter the API key
        args = request.args
        lon = str(args.get('lon'))
        lat = str(args.get('lat'))
        
        url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}'
        response = requests.get(url).json()
        return jsonify(response),200

    except Exception as e:
      raise Exception("Something bad happened")