print("http://localhost:8000/")
#----------------------------------------------
# Importing
#----------------------------------------------
from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os
from waitress import serve 

# Email validation 
import re

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
    return render_template('GENERIC/FRONT-PAGE.html')

@app.route('/HOMEPAGE')
def HOMEPAGE():
    return render_template('GENERIC/HOME-PAGE.html')

#----------------------------------------------
# Login 
#----------------------------------------------
@app.route('/LOGIN', methods={"POST","GET"})
def LOGIN():
    if request.method == "POST":
        displayName=request.form["displayName"]
        email=request.form["email"]
        inserted_password=request.form["password"]

        checked_user = dbHandler.retreiveUser(displayName,email,inserted_password)
        
        if checked_user:
            return redirect(url_for('HOMEPAGE'))
        else:
            return render_template('GENERIC/LOGIN.html')
    else:    
        return render_template('GENERIC/LOGIN.html')
    








#----------------------------------------------
# Registration 
#----------------------------------------------
@app.route('/REGISTER', methods={"POST","GET"})
def REGISTER():
    if request.method == "POST":

        displayName = request.form["displayName"]
        email = request.form["email"]
        password = request.form["password"]

#-----------------------------------------------------------
# Email Validation 
#-----------------------------------------------------------

        student_pattern = r"^[a-zA-Z0-9._%+-]+@education\.nsw\.gov\.au$"
        teacher_pattern = r"^[a-zA-Z0-9._%+-]+@det\.nsw\.edu\.au$"

        if re.match(student_pattern,email):
            account_type = "student"
        elif re.match(teacher_pattern,email):
            account_type = "teacher"
        else:
            print("error -not accepted domain")
            return render_template("GENERIC/REGISTER.html",error="This isnt a accepted email domain")
            #Show the error that this isnt a valid email. 
        
        if dbHandler.emailExists(email):
            print("error - email used already")
            return render_template("GENERIC/REGISTER.html",error="This email is already registered.")
            
#-------------------------------------------------------------------
# HASHING PASSWORDS
#-------------------------------------------------------------------
        hash = bcrypt.generate_password_hash(password).decode('utf-8')
#--------------------------------------------------------------------
# INSERTING INTO DATABASE
#--------------------------------------------------------------------
        dbHandler.insertUser(displayName,email,hash)
        return render_template("GENERIC/FRONT-PAGE.html")
    else:
        return render_template("GENERIC/REGISTER.html")




if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=8000)

