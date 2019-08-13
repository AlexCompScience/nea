import sqlite3
import random
from difflib import SequenceMatcher


def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def game(userID):
    print(userID)
    with sqlite3.connect('table.db') as db:
        cursor = db.cursor()
        points = 0
        currentgoes = 2
        i = True
        cursor.execute('SELECT * FROM songs')
        songs = cursor.fetchall()
        while currentgoes > 0 and i:
            if len(songs) == 0:
                i = False
                break
            song = random.choice(songs)
            print('song', song)
            choice = input('The artist of this song is ' + song[1] + ' and your clue is ' + song[
                3] + '.\nGuess the title of the song.\n')
            value = similar(choice.lower(), song[2].lower())
            if value > 0.8:
                print('\n\nThat was correct!\n\n')
                if currentgoes == 2:
                    points += 3
                elif currentgoes == 1:
                    points += 1
                songs.remove(song)
            else:
                if currentgoes == 1:
                    i = False
                currentgoes -= 1
                print('\n\nThat was incorrect! You have ' + str(currentgoes) + ' goes left!')
        print('You scored ' + str(points) + ' points!')
        cursor.execute('''SELECT * FROM scores WHERE userID=?''', [userID])
        g = cursor.fetchall()
        print('scores', g)
        if g:
            cursor.execute('''UPDATE scores SET score=? WHERE userID=?''', [(g[0][2] + points), userID])
        else:
            cursor.execute('''INSERT INTO scores(userID,score)
            VALUES(?,?)''', [userID, points])