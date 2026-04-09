print("http://localhost:8000/")

# Importing  ----------------------------------------------------------------------------------------------------------------------------------------------------------------->

from flask import Flask, render_template, request, redirect, session, url_for
import sqlite3
import os
from waitress import serve 
import datatabase_Initiation as dbInit
import database_Managment as dbHandler


#Creating the Database
dbInit.init_db()

app = Flask(__name__)
app.secret_key = os.urandom(24)

@app.route('/')
def FRONTPAGE():
    return render_template('FRONT-PAGE.html')

@app.route('/LOGIN')
def LOGIN():
    return render_template('LOGIN.html')

@app.route('/REGISTER')
def REGISTER():
    return render_template('REGISTER.html')

if __name__ == '__main__':
    serve(app, host="0.0.0.0", port=8000)

