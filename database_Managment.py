import sqlite3 as sql
import html
import time
import random
from flask_bcrypt import Bcrypt 

bcrypt = Bcrypt()

#---------------- 
# Inserting users
#----------------
def insertUser(username,hash):
    con = sql.connect("database_Files/Database.db")
    cur = con.cursor

    cur.execute("INSERT INTO users (username,password) VALUES (?,?,?)", (username, hash,),)
    con.commit()
    con.close()
    