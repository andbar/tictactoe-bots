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
        if self.me == "X":
            self.first = True
        else:
            self.first = False
        row_one = row1
        row_two = row2
        row_three = row3
        self.board = self.create_board(row_one, row_two, row_three)
        self.columns = [[row_one[0], row_two[0], row_three[0]],
                        [row_one[1], row_two[1], row_three[1]],
                        [row_one[2], row_two[2], row_three[2]]
                        ]
        self.diagonals = [[row_one[0], row_two[1], row_three[2]],
                          [row_one[2], row_two[1], row_three[0]]
                         ]

    def create_board(self, row_one, row_two, row_three):
        return [row_one, row_two, row_three]

    #def create_columns(self, board):
    #    column1 = []
    #    column2 = []
    #    column3 = []
    #    for row in board:
    #        for ind, val in enumerate(row):
    #            column1.append(row[0])
    #            column2.append(row[1])
    #            column3.append(row[2])
    #    return [column1, column2, column3]



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


class Better_Bot(TicTacToe_Bot):

    def decide_move(self):
        pass

    #def strategy(self):
    #    if self.first == True:
    #        print("You are first")
    #    else:
    #        print("You are O's")

    def win_or_block(self, board, player):
        for index, row in enumerate(board):
            count = 0
            open_spots = []
            for ind, spot in enumerate(row):
                if spot == player:
                    count += 1
                if spot == "_":
                    open_spots.append(ind)
            if count == 2 and len(open_spots) == 1:
                return (index, open_spots[0])

    def winning_row(self):
        return self.win_or_block(self.board, self.me)

    def winning_column(self):
        return self.win_or_block(self.columns, self.me)

    def winning_diagonal(self):
        return self.win_or_block(self.diagonals, self.me)

    def blocking_row(self):
        return self.win_or_block(self.board, self.you)

    def blocking_column(self):
        return self.win_or_block(self.columns, self.you)

    def blocking_diagonal(self):
        return self.win_or_block(self.diagonals, self.you)

    def winning_move(self):
        win_row = self.winning_row()
        win_col = self.winning_column()
        win_diag = self.winning_diagonal()
        if type(win_row) == tuple:
            return win_row
        if type(win_col) == tuple:
            return win_col
        if type(win_diag) == tuple:
            return win_diag

    def blocking_move(self):
        block_row = self.blocking_row()
        block_col = self.blocking_column()
        block_diag = self.blocking_diagonal()
        if type(block_row) == tuple:
            return block_row
        if type(block_col) == tuple:
            return block_col
        if type(block_diag) == tuple:
            return block_diag






randy = Random_Bot(team, first_row, second_row, third_row)
randy.decide_move()
