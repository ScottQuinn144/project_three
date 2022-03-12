import random
import sys


def create_random_ship():
    '''
    Creates a random position within the board to place the target
    '''
    return random.randint(0, 5), random.randint(0, 5)


def play_again():
    '''
    Start a new game or exit the program
    '''
    another_game = input("Wanna play again? <y>es or <n>o? >: ").lower()
    if another_game == "y":
        play_game()
    else:
        print("Goodbye!")
        sys.exit()


def play_game():
    '''
    Guesses and checks with data validation
    '''
    print('3')


create_random_ship()
play_again()
play_game()
