from sys import exit


def menu(userID):
    _ = True
    while _:
        choice = input('''Welcome to the Music Quiz Menu. Please choose what you would like to do.
        1 - See my Stats
        2 - Play A Game
        3 - Log Out
        ''')
        if int(choice) == 1:
            from seeStats import see_stats
            see_stats(userID)
        elif int(choice) == 2:
            from playGame import game
            game(userID)
        elif int(choice) == 3:
            exit()
        else:
            print('Invalid syntax.')