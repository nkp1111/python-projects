class Board:

    def __init__(self):
        self.board = [" "] * 9
        self.format_board()

    def format_board(self):
        for i, val in enumerate(self.board):
            if i % 3 == 0:
                self.board[i] = "\n|" + self.board[i]

    def print_board(self):
        print("|".join(self.board) + "|")


