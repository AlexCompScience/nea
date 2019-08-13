import sqlite3


def login():
    f = True
    while f:
        user = input("Enter your username:\n")
        pword = input("Enter your password:\n")

        with sqlite3.connect("table.db") as db:
            cursor = db.cursor()
            find_user = (
                'SELECT * FROM users WHERE username = ? AND password = ?')
            cursor.execute(find_user, [user, pword])
            results = cursor.fetchall()
            if results:
                result = results[0]
                print('Welcome ' + result[1] + ' ' + result[2] + '.')
                f = False
                from loggedInMenu import menu
                menu(result[0])
            else:
                print('Username and password not correct.')
                again = input('Do you want to retry? (y/n)')
                if again.lower() == 'n':
                    print('Goodbye')
                    f = False


login()
