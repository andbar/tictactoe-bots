import random


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
        self.corners = [self.board[0][0], self.board[0][2], self.board[2][2],
                        self.board[2][0]
                        ]

    def create_board(self, row_one, row_two, row_three):
        return [row_one, row_two, row_three]

    def what_move(self, board):
        count = 0
        for row in board:
            for r in row:
                if r == "_":
                    count += 1
        return count

    def open_corners(self, corners):
        open_corners = []
        for index, corner in enumerate(corners):
            if corner == "_":
                open_corners.append(index)
        return open_corners

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

    def third_move(self, board):
        if self.board[1][1] == "O":
            print("{} {}".format(0, 2))
        elif self.board[2] == "X__":
            print("{} {}".format(2, 2))
        else:
            print("{} {}".format(0, 0))

    def fourth_move(self, board):
        if self.board[0][0] == "X" and self.board[2][2] == "X":
            print("{} {}".format(2, 1))
        elif self.board[2][0] == "X" and self.board[0][2] == "X":
            print("{} {}".format(2, 1))
        elif self.board[1][0] == "X" and self.board[1][2] == "X":
            print("{} {}".format(2, 0))
        elif self.board[0][1] == "X" and self.board[2][1] == "X":
            print("{} {}".format(2, 0))
        elif self.board[1][1] == "X" and self.board[0][2] == "X":
            print("{} {}".format(2, 2))
        elif self.board[2][0] == "X" and self.board[0][1] == "X":
            print("{} {}".format(0, 0))
        elif self.board[2][0] == "X" and self.board[1][2] == "X":
            print("{} {}".format(2, 2))
        elif self.board[0][0] == "X" and self.board[2][1] == "X":
            print("{} {}".format(2, 0))
        elif self.board[0][0] == "X" and self.board[1][2] == "X":
            print("{} {}".format(0, 2))
        elif self.board[0][2] == "X" and self.board[2][1] == "X":
            print("{} {}".format(2, 2))
        elif self.board[0][2] == "X" and self.board[1][0] == "X":
            print("{} {}".format(0, 0))
        elif self.board[0][1] == "X" and self.board[2][2] == "X":
            print("{} {}".format(0, 2))
        elif self.board[1][0] == "X" and self.board[2][2] == "X":
            print("{} {}".format(2, 0))
        elif self.board[0][1] == "X" and self.board[1][0] == "X":
            print("{} {}".format(0, 0))
        elif self.board[0][1] == "X" and self.board[1][2] == "X":
            print("{} {}".format(0, 2))
        elif self.board[1][0] == "X" and self.board[2][1] == "X":
            print("{} {}".format(2, 0))
        elif self.board[2][1] == "X" and self.board[1][2] == "X":
            print("{} {}".format(2, 2))
        else:
            self.random_move()

    def fifth_move(self):
        open_corners = self.open_corners(self.corners)
        if open_corners == [0]:
            print("{} {}".format(0, 0))
        elif open_corners == [1]:
            print("{} {}".format(0, 2))
        elif open_corners == [2]:
            print("{} {}".format(2, 2))
        elif open_corners == [3]:
            print("{} {}".format(2, 0))
        else:
            print("{} {}".format(1, 1))

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
            move = self.what_move(self.board)
            if move == 9:
                print("{} {}".format(2, 0))
            elif move == 8:
                if self.board[1][1] == "_":
                    print("{} {}".format(1, 1))
                else:
                    print("{} {}".format(2, 0))
            elif move == 7:
                self.third_move(self.board)
            elif move == 6:
                self.fourth_move(self.board)
            elif move == 5:
                self.fifth_move()
            else:
                self.random_move()
