import sqlite3 as sql
def init_db():
    con = sql.connect("database_files/database.db")
    cur = con.cursor()

    cur.execute(""" 
                CREATE TABLE IF NOT EXISTS users(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    displayName TEXT NOT NULL,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL
                ) """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS questions(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                question TEXT NOT NULL,
                answer TEXT NOT NULL
                ) """)

    cur.execute("""
                CREATE TABLE IF NOT EXISTS class_message_board(
                message TEXT NOT NULL, 
                reply TEXT
                )""")

    cur.execute("""
                CREATE TABLE IF NOT EXISTS priv_message_board(
                message TEXT NOT NULL, 
                reply TEXT
                )""")
    
    cur.execute("""
                CREATE TABLE IF NOT EXISTS classroom(
                school TEXT NOT NULL,
                teacher TEXT NOT NULL, 
                students TEXT
                )""")

    con.commit()
    con.close()


