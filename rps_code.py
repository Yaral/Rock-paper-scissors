# -*coding:utf-8-*-
import time
from time import sleep
import random

sus = "-" * 35 #line separator
data = ["paper", "scissors", "rock"]
while True:
    x = input("Choose your option, rock, paper or scissors: ")
    if x not in data:
        print("Choose correctly")
        continue

    pc = random.choice(data)
    sleep(0.5)

    print(("The pc choose {} ").format(pc))
    if x == pc:
        print("Tie!")
    elif x == "scissors" and pc == "paper":
        print("You won!")
    elif x == "paper" and pc == "rock":
        print("You won!")
    elif x == "rock" and pc == "scissors":
        print("You won!")
    else:
        print("We lost. {} wins {} \n".format(pc, x))
    print(sus)
