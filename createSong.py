import sqlite3


def createsong():
    with sqlite3.connect('table.db') as db:
        cursor = db.cursor()
        artist = input('Please enter the song artist. ')
        songtitle = input('Please enter the song title. ')
        firstletters = input('Please enter the first letter of each word, separated by spaces. ')
        insert_data = '''INSERT INTO songs(artist,title,firstLetterOfEachWord)
            VALUES(?,?,?)'''
        cursor.execute(
            insert_data, [artist, songtitle, firstletters])
        db.commit()


createsong()
