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


class Better_Bot(TicTacToe_Bot):

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
        win_row = self.win_or_block(self.board, self.me)
        if win_row:
            return win_row
        else:
            return False

    def winning_column(self):
        win_col = self.win_or_block(self.columns, self.me)
        if win_col:
            return (win_col[1], win_col[0])
        else:
            return False

    def winning_diagonal(self):
        win_diag = self.win_or_block(self.diagonals, self.me)
        if win_diag:
            if win_diag == (1, 0):
                return (0, 2)
            elif win_diag == (1, 2):
                return (2, 0)
            elif win_diag == (1, 1):
                return win_diag
            else:
                return (win_diag[1], win_diag[1])
        else:
            return False

    def blocking_row(self):
        block_row = self.win_or_block(self.board, self.you)
        if block_row:
            return block_row
        else:
            return False

    def blocking_column(self):
        block_col = self.win_or_block(self.columns, self.you)
        if block_col:
            return (block_col[1], block_col[0])
        else:
            return False

    def blocking_diagonal(self):
        block_diag = self.win_or_block(self.diagonals, self.you)
        if block_diag:
            if block_diag == (1, 0):
                return (0, 2)
            elif block_diag == (1, 2):
                return (2, 0)
            elif block_diag == (1, 1):
                return block_diag
            else:
                return (block_diag[1], block_diag[1])
        else:
            return False

    def winning_move(self):
        win_row = self.winning_row()
        win_col = self.winning_column()
        win_diag = self.winning_diagonal()
        if win_row:
            return win_row
        elif win_col:
            return win_col
        elif win_diag:
            return win_diag
        else:
            return False

    def blocking_move(self):
        block_row = self.blocking_row()
        block_col = self.blocking_column()
        block_diag = self.blocking_diagonal()
        if block_row:
            return block_row
        elif block_col:
            return block_col
        elif block_diag:
            return block_diag
        else:
            return False

    def random_move(self):
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if self.board[row][col] == "_":
            print("{} {}".format(row, col))
        else:
            self.random_move()

    def decide_move(self):
        win = self.winning_move()
        block = self.blocking_move()
        if win:
            print("{} {}".format(win[0], win[1]))
        elif block:
            print("{} {}".format(block[0], block[1]))
        else:
            self.random_move()

betbot = Better_Bot(team, first_row, second_row, third_row)
betbot.decide_move()
