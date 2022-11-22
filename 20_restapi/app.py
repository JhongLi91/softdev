"""
Kung Pao Chicken: Brian Yang, Jian Hong li
SoftDev
k20 -- RESTful API
2022 -- 11 -- 21
time spent: .5 hours
"""

from flask import Flask, render_template
import requests

app = Flask(__name__)    #create Flask object


@app.route("/")
def index():
    try: #check for if key_nasa.txt exists
        with open("key_nasa.txt", "r") as file:
            api_key = file.read()
            request_data = requests.get("https://api.nasa.gov/planetary/apod?api_key=" + api_key) #returns a requests.models.Response class that need to be made into a json
            data = request_data.json()
            image = data["hdurl"] #Select the thing we want from the json
            return render_template('main.html', img = image)
    except:
        return render_template('main.html', error = "No/Wrong API key provided")


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
