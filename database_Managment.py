import sqlite3 as sql
import html
import time
import random
from flask_bcrypt import Bcrypt 
bcrypt = Bcrypt()
#---------------- 
# Inserting users
#----------------
def insertUser(displayName,email,password_hash,account_type):
    con = sql.connect("database_Files/database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO users (displayName,email,password,role) VALUES (?,?,?,?)", (displayName, email, password_hash, account_type),)
    con.commit()
    con.close()

#-----------------
# Retreiving Users
#-----------------
def retreiveUser(displayName,email,inserted_password):
    con = sql.connect("database_Files/database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM users WHERE displayName == ? AND email == ?", (displayName,email)) 
    user = cur.fetchone()

    con.close()
    return user

#--------------------------
# Checking exisiting emails
#--------------------------
def emailExists(email):
    con = sql.connect("database_Files/database.db")
    cur = con.cursor()

    query = "SELECT 1 FROM users WHERE EMAIL = ? LIMIT 1"
    cur.execute(query,(email,))
    exists = cur.fetchone() is not None

    con.close()
    return exists

#--------------------------
# Adding CLASSROOM messages / reply to database
#--------------------------
def add_Class_message(class_id, user_id, text):
    con = sql.connect("database_Files/database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO class_message_board(class_id, user_id, message) values (?,?,?)", (class_id, user_id, text,))
    con.commit()
    con.close()

def retrieve_Class_Message(class_id):
    con = sql.connect("database_Files/database.db")
    cur = con.cursor()

    cur.execute("SELECT * FROM class_message_board WHERE class_id = ?;" (class_id,))
    rows = cur.fetchall()
    con.close()
    return rows



#-------------------------------------------------------------------------------------------------------------------

