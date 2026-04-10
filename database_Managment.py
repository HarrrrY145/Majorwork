import sqlite3 as sql
import html
import time
import random
from flask_bcrypt import Bcrypt 

#---------------- 
# Inserting users
#----------------
def insertUser(username,email,hash):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor()

    cur.execute("INSERT INTO users (displayName,email,password) VALUES (?,?,?)", (username, email, hash),)
    con.commit()
    con.close()
