"""
TicTacToe game
This is terminal based tictactoe game.
"""
from art import logo
from game import TicTacToe
from time import sleep


def game_rule():
    print("The positions are structured like:")
    print("""
    |0|1|2|
    |3|4|5|
    |6|7|8|
    """)
    sleep(1)


game_board = TicTacToe()

print("\nWelcome to the Tic Tac Toe game. ")
print(logo)
sleep(1)

print()
print("Press 'h' for help for positions on board")
print()

while not game_board.winner:
    sleep(1)
    print(f"\nIt's {game_board.current} turn.\n")
    print(f"The available choices are : {game_board.choices}")

    if game_board.current != "player":
        position = game_board.computer_move()
    else:
        position = input("Choose a position 0 to 8 or h: ")

    if position.lower() == "h":
        game_rule()
    elif position not in game_board.choices:
        print("Put a valid position between 0 - 8. That has not been filled.\n")
    else:
        game_board.handle_moves(position)
        game_board.print_board()
        if game_board.check_winner("player"):
            print("\nWinner is player.\n")
        elif game_board.check_winner("computer"):
            print("\nWinner is computer.\n")

if game_board.winner == "Draw":
    print("Games over for this round...")
    print("Its draw\n")

