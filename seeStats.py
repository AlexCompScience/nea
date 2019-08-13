import sqlite3
from sys import exit


def see_stats(userid):
    with sqlite3.connect("table.db") as db:
        cursor = db.cursor()
        while True:
            choice = input('''Whose statistics would you like to see?
            1 - Top 5 Users
            2 - Me
            3 - Exit
            ''')
            if int(choice) == 1:
                cursor.execute('''SELECT * FROM scores ORDER BY score DESC LIMIT 5''')
                results1 = cursor.fetchall()
                results = [list(res) for res in results1]

                i = 1
                for result in results:
                    print(str(i) + ' - ' + str(result[2]) + ' points!')
                    i += 1
            elif int(choice) == 2:
                cursor.execute('''SELECT * FROM scores WHERE userID=?''', [userid])
                res = cursor.fetchall()
                if not res:
                    print('You have not scored any points.')
                else:
                    print('You got', str(res[0][2]), 'points!')
            else:
                exit()
