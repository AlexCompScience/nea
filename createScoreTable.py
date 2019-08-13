import sqlite3
with sqlite3.connect('table.db') as db:
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS scores(
            ID INTEGER PRIMARY KEY,
            userID INTEGER,
            score INTEGER
        );
    ''')
