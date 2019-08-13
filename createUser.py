import sqlite3


def createuser():
    with sqlite3.connect('table.db') as db:
        cursor = db.cursor()
        f = True
        while f:
            username = input("Please enter a username.")
            firstname = input("Please enter your first name.")
            lastname = input("Please enter your last name.")
            pass1 = input("Please enter a password.")
            pass2 = input("Please reenter the password.")
            if pass1 != pass2:
                print('Passwords do not match.')
            else:
                find_user = 'SELECT * FROM users WHERE username = ?'
                cursor.execute(find_user, [username])
                if cursor.fetchall():
                    print('Username taken.')
                else:
                    insert_data = '''INSERT INTO users(username,firstname,lastname,password)
                        VALUES(?,?,?,?)'''
                    cursor.execute(insert_data, [username, firstname, lastname, pass1])
                    db.commit()
                    f = False
