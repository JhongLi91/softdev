from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate sessions!
from flask import redirect

#______________________
app = Flask(__name__)    #create Flask object

@app.route("/", methods=['GET'])
def index():
    api = request.form.get("url")
    return render_template("main.html", )


if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
