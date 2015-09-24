import random


team = input()
first_row = input()
second_row = input()
third_row = input()


class TicTacToe_Bot:

    def __init__(self, me, row1, row2, row3):
        self.me = me
        if self.me == "X":
            self.you = "O"
        else:
            self.you = "X"
        row_one = row1
        row_two = row2
        row_three = row3
        self.board = self.create_board(row_one, row_two, row_three)

    def create_board(self, row_one, row_two, row_three):
        return [row_one, row_two, row_three]

    def decide_move(self):
        raise NotImplementedError("Decide move must be implemented in subclass")


class Random_Bot(TicTacToe_Bot):

    def decide_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if self.board[row][col] not in "XO":
            print("{} {}".format(row, col))
        else:
            self.decide_move()


#class Better_Bot(TicTacToe_Bot):






randy = Random_Bot(team, first_row, second_row, third_row)
randy.decide_move()
