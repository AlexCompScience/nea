from sys import exit


def loginmenu():
    _ = True
    while _:
        choice = input('''Welcome to the Login Menu. Please choose what you would like to do.
        1 - Log in to an existing account
        2 - Create a new account
        3 - Exit
        ''')
        if int(choice) == 1:
            from loginUser import login
            login()
        elif int(choice) == 2:
            from createUser import createuser
            createuser()
        elif int(choice) == 3:
            exit()
        else:
            print('Invalid syntax.')


loginmenu()
