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


@app.route('/HOMEPAGE', methods ={"GET", "POST"})
def HOMEPAGE():
    return render_template('GENERIC/HOME-PAGE.html')

@app.route('/PROGRESS_ANALYTICS')
def PROGRESS_ANALYTICS():
    return render_template('STUDENT/PROGRESS_ANALYTICS.html')

@app.route('/CLASSROOM')
def CLASSROOM():
    return render_template('TEACHER/CLASSROOM.html')

@app.route('/ACTIVITIES')
def ACTIVITIES():
    return render_template('STUDENT/ACTIVITIES.html')

@app.route('/PRACTICE_TESTS')
def PRACTICE_TESTS():
    return render_template('STUDENT/PRACTICE_TESTS.html')

@app.route('/MODULES')
def MODULES():
    return render_template('MODULES/MODULES.html')

@app.route('/MESSAGE_BOARD/<int:class_id>')
def MESSAGE_BOARD(class_id):
    messages = dbHandler.retrieve_Class_Message(class_id)
    return render_template('TEACHER/CLASSROOM_MESSAGE_BOARD.html', text=messages)

#----------------------------------------------
# Login 
#----------------------------------------------
@app.route('/LOGIN', methods={"POST","GET"})
def LOGIN():
    if request.method == "POST":
        displayName=request.form["displayName"]
        email=request.form["email"]
        inserted_password=request.form["password"]

        user = dbHandler.retreiveUser(displayName,email)


        #------------------------------
        # Checking the hashed passwords
        #------------------------------
        if user and bcrypt.check_password_hash(user[3],inserted_password):
            # User Session 
            session["user_id"] = user[0]
            session["role"] = user[4]
            return redirect(url_for('HOMEPAGE'))
        else:
            return render_template('GENERIC/LOGIN.html')
    else:    
        return render_template('GENERIC/LOGIN.html')




#----------------------------------------------
# Class Message Board
#----------------------------------------------
# Adding texts to the database
@app.route('/CLASSROOM_MESSAGE_BOARD/<int:class_id>', methods={"POST", "GET"})
def add_message(class_id):

    if request.method == "POST":
        text = request.form.get('message')

        if text and text.strip():
            dbHandler.add_Class_message(class_id, session["user_id"], text.strip())

        return redirect(url_for('MESSAGE_BOARD'))







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
        dbHandler.insertUser(displayName,email,hash,account_type)
        return render_template("GENERIC/FRONT-PAGE.html")
    else:
        return render_template("GENERIC/REGISTER.html")




if __name__ == '__main__':
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=8000)


