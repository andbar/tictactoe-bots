import random

from andy_bot import Better_Bot


team = input()
first_row = input()
second_row = input()
third_row = input()

gamebot = Better_Bot(team, first_row, second_row, third_row)
gamebot.decide_move()
