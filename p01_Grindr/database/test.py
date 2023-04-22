from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission
from flask import session           #facilitate sessions!
from flask import redirect
import os                           #facilitate key generation
import sqlite3
from db_tool import * #imports account creation functions from accounts_db.py


#______________________
app = Flask(__name__)    #create Flask object
app.secret_key= os.urandom(32) #create random secret key
#print(app.secret_key)


@app.route("/", methods=['GET']) #, methods=['GET', 'POST'])
def index():
    if 'username' in session:   #if already logged in
        return redirect('/home') # username=session['username'], password=session['password'], request_method = "GET")
    else:                       #if not logged in, send user to login page
        return render_template('login.html')


@app.route("/login", methods=['GET','POST'])
def authenticate():
    if (request.method == "POST"):
        session['username']= request.form.get('username')   #remember user in session
        session['password'] = request.form.get('password')  #remember user in session
        if( check(request.form['username'], request.form['password'])):
            return redirect('/home')
        else:
            return render_template('login.html', exception =  "Authentication failed, try again")
    else:
        if(session != {}):
            return redirect("/home")
        else:
            return render_template('login.html')

@app.route("/register", methods = ['GET','POST'])
def register():
    if (request.method == "POST"):
        if (request.form.get('password1') != request.form.get('password2')):
            return render_template("register.html", exception = "Passwords don't match")
        elif (request.form.get('password1') == ""):
            return render_template("register.html", exception = "Password can't be empty!")
        else:
            if (create_acc(request.form['username'], request.form['password1'])): #True IF another account exist, false if no problems
                return render_template("register.html", exception = "Username taken!")
        return render_template("login.html")
    else:
        return render_template("register.html")

if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True
    app.run()
