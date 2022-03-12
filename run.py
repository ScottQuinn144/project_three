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
    another_game = input("Wanna play again? <y>es or <n>o?: ").lower()
    if another_game == "y":
        play_game()
    else:
        print("Goodbye!")
        sys.exit()


print("Welcome to Battleships!")
print("""\nYou have 15 missles and there are 3 ships on the map.
In order to hit them, you have to enter specific numbers for that location.
Example: For the first row and first column, you have to write 1 and 1.
\nGOODLUCK!\n""")


def play_game():
    '''
    Guesses and checks with data validation
    '''
    print('3')


create_random_ship()
play_again()
play_game()
