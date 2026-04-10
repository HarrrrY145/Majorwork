print("http://localhost:8000/")

# Importing  ----------------------------------------------------------------------------------------------------------------------------------------------------------------->

from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os
from waitress import serve 

# Hashing Imports
from flask_bcrypt import Bcrypt 

# Database imports
import datatabase_Initiation as dbInit
import database_Managment as dbHandler

app = Flask(__name__)

#Creating the Database
dbInit.init_db()

app = Flask(__name__)
app.secret_key = os.urandom(24)
bcrypt = Bcrypt(app)



@app.route('/')
def FRONTPAGE():
    return render_template('FRONT-PAGE.html')

@app.route('/LOGIN')
def LOGIN():
    return render_template('LOGIN.html')

@app.route('/REGISTER', methods={"POST","GET"})
def REGISTER():
    if request.method == "POST":
        displayName = request.form["displayName"]
        email = request.form["email"]
        password = request.form["password"]
#-------------------------------------------------------------------
# HASHING PASSWORDS
#-------------------------------------------------------------------
        hash = bcrypt.generate_password_hash(password).decode('utf-8')
#--------------------------------------------------------------------
# INSERTING INTO DATABASE
#--------------------------------------------------------------------
        dbHandler.insertUser(displayName,email,hash)
        return render_template("/FRONT-PAGE.html")
    else:
        return render_template("REGISTER.html")



    return render_template('REGISTER.html')

if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=8000)

