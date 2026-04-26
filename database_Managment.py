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
    
#--------------------------
# Checking exisiting emails
#--------------------------
def emailExists(email):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    query = "SELECT 1 FROM users WHERE EMAIL = ? LIMIT 1"
    cur.execute(query,(email,))
    exists = cur.fetchone() is not None

    con.close()
    return exists

#--------------------------
# Adding CLASSROOM messages / reply to database
#--------------------------
def add_Class_message(text):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO class_message_board(message) values (?)", (text,))
    con.commit()
    con.close()

def retrieve_Class_Message():
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM class_message_board;")
    rows = cur.fetchall()

    con.close()
    return rows



#-------------------------------------------------------------------------------------------------------------------
def add_Class_reply(reply):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO class_message_board(reply) values (?)" (reply))
    con.close()

