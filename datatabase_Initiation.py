import sqlite3 as sql
def init_db():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    cur.execute(""" 
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    displayName TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                ) """)
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS questions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
                ) """)
    con.commit()
    con.close()

    