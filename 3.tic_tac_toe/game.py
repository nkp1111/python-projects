import random


class TicTacToe:

    def __init__(self):
        self.board = [" "] * 9
        self.format_board()
        self.player = []
        self.computer = []
        self.win_condition = ["012", "345", "678", "036", "147", "258", "048", "246"]
        self.winner = None
        self.current = "player"
        self.choices = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    def format_board(self):
        """
        Format the board to appear visually like a 3 x 3 grid
        :return: None
        """
        for i, val in enumerate(self.board):
            if i % 3 == 0:
                self.board[i] = "\n|" + self.board[i].replace("|", "").replace("\n", "")

    def print_board(self):
        """
        Print board on terminal
        :return: None
        """
        self.format_board()
        print("|".join(self.board) + "|")

    def computer_move(self):
        """
        Choose one of the available options
        :return: String
        """
        return random.choice(self.choices)

    def handle_moves(self, choice):
        """
        Responsible for putting choice on board for the current player.
        :param choice:
        :return:
        """
        if self.current == "player":
            self.current = "computer"
            self.board[int(choice)] = "X"
            self.player.append(choice)
        else:
            self.current = "player"
            self.board[int(choice)] = "O"
            self.computer.append(choice)

        self.choices.remove(choice)
        if len(self.choices) == 0:
            self.winner = "Draw"

    def check_winner(self, target):
        """
        Responsible for checking if the current target won the game.
        :param target:
        :return:
        """
        self.player.sort()
        self.computer.sort()

        if target == "player":
            check = self.player
        else:
            check = self.computer

        res = ""
        for i in check:
            res += i
            for j in check:
                if j not in res and len(res) < 3:
                    res += j
                    for k in check:
                        if k not in res and len(res) < 3:
                            res += k

            if res in self.win_condition:
                self.winner = target
                return True
            else:
                res += ""




