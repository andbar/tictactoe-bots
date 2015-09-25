import random

from andy_bot import Random_Bot


team = input()
first_row = input()
second_row = input()
third_row = input()

randy = Random_Bot(team, first_row, second_row, third_row)
randy.decide_move()
