import sqlite3
with sqlite3.connect('table.db') as db:
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            userID INTEGER PRIMARY KEY,
            firstname VARCHAR(20),
            lastname VARCHAR(20),
            username VARCHAR(20),
            password VARCHAR(20)
        );
    ''')