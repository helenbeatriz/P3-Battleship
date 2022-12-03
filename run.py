import gspread
from google.oauth2.service_account import Credentials
from random import randint
import os
import sys

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('battleship_names')


#  Welcome message and rules
def welcome():
    os.system('clear')
    print("Welcome to Battleships!")
    print("Our board consists of 8 rows and 8 columns.")
    print("Your goal is to find where the ships are")
    print("After every input you type a row and a column letter ")
    print("into the game, press enter to continue.")
    print("Whenever you get it right an 'X' will be displayed")
    print("Whenever you get it wrong an '-' will be displayed")
#  Board for holding ship locations

HIDDEN_BOARD = [[" "] * 8 for x in range(8)]
#  Board for displaying hits and misses
GUESS_BOARD = [[" "] * 8 for i in range(8)]


def print_board(board):
    print("  A B C D E F G H")
    print("  +-+-+-+-+-+-+-+")
    row_number = 1
    for row in board:
        print("%d|%s|" % (row_number, "|".join(row)))
        row_number += 1


letters_to_numbers = {
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7
}
# computer create 5 ships


def create_ships(board):
    for ship in range(5):
        ship_row, ship_column = randint(0, 7), randint(0, 7)
        while board[ship_row][ship_column] == "X":
            ship_row, ship_column = get_ship_location()
        board[ship_row][ship_column] = "X"


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGH":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]


# check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count


def game():
    create_ships(HIDDEN_BOARD)
    turns = 10
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)
        row, column = get_ship_location()
        if GUESS_BOARD[row][column] == "-":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X"
            turns -= 1
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"
            turns -= 1
        if count_hit_ships(GUESS_BOARD) == 5:
            print("You won!")
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You lost :( !! ")


# Calling function for the game
if __name__ == "__main__":
    welcome()
    game()
