from flask import Flask
from flask import render_template
import urllib.request, json

#______________________
app = Flask(__name__)    #create Flask object

@app.route("/")
def index():
    key = open("key_nasa.txt").read()
    url = "https://api.nasa.gov/planetary/apod?api_key=" + key
    return render_template("main.html", url = url)


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
