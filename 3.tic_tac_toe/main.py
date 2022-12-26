"""
TicTacToe game
This is terminal based tictactoe game.
"""
from art import logo
from board import Board


def game_rule(self):
    print("The positions are structured like:")
    print("""
    |0|1|2|
    |3|4|5|
    |6|7|8|
    """)


print("\nWelcome to the Tic Tac Toe game. ")
print(logo)

game_board = Board()

game_board.print_board()
print()

print("It's player1 turns.")
position = input("Name a position 0 to 8: ")
