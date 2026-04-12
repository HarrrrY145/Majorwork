import sqlite3 as sql
import html
import time
import random
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()
#---------------- 
# Inserting users
#----------------
def insertUser(displayName,email,hash):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO users (displayName,email,password) VALUES (?,?,?)", (displayName, email, hash),)
    con.commit()
    con.close()

#-----------------
# Retreiving Users
#-----------------
def retreiveUser(displayName,email,inserted_password):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE displayName == ? AND email == ?", (displayName,email)) 
    user = cur.fetchone()

    if user is None: # No user found
        con.close()
        return False
    
#------------------------------
# Checking the hashed passwords
#------------------------------
    stored_hash = user[3]
    if bcrypt.check_password_hash(stored_hash,inserted_password):
        con.close()
        return True
    else:
        con.close()
        return False