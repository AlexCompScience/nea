import sqlite3
with sqlite3.connect('table.db') as db:
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS songs(
            songID INTEGER PRIMARY KEY,
            artist VARCHAR(64),
            title VARCHAR(64),
            firstLetterOfEachWord VARCHAR(64)
        );
    ''')
