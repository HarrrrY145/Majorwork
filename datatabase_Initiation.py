import sqlite3 as sql
def init_db():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    cur.execute(""" 
                CREATE TABLE IF NOT EXISTS users(
                    username PRIMARY KEY TEXT NOT NULL,
                    password TEXT NOT NULL,
                 ) """)
    con.commit()
    con.close()