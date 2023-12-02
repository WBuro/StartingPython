import sys
import random
from enum import Enum

#constant variables

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

""" print(RPS(2))
print(RPS.ROCK)
print(RPS['ROCK'])
print(RPS.ROCK.value)
sys.exit() """

print("")
playerchoice = input("Enter ... \n1 for Rock,\n2 for Paper,\n3 for Scissors,\n\n")
print(playerchoice)

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1,2 or 3 ")


computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You choose " + str(RPS(player)).replace('RPS.' , ' ' ) + ".") #terminalde RPS yazısıda çıkıyor o da gitti
print("Python choose: " + str(RPS(computer)).replace('RPS.' , ' ') + ".")
print("")

if player == 1 and computer == 3:
    print("🎉 You Lose!")
elif player == 2 and computer == 1:
    print("🎉 You Win!")
elif player == 3 and computer == 2:
    print("🎉 You Win!")
elif player == computer:
    print("😯 Tie Gme!")
else:
    print("🐍 Python Wins!")