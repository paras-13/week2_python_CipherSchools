# To make a number guessing game

from random import randint as r
r_num = r(0,100)
flag = "down"
times = 0
u_num = int(input("Guess a number a between 0 1nd 100 : "))
while flag == "down":
    if u_num < r_num:
        print("Too low")
        times +=1
        u_num = int(input("Guess again : "))
        flag = "down"
    elif u_num > r_num:
        print("Too high")
        u_num = int(input("Guess Again : "))
        flag = "down"
        times +=1
    else:
        times +=1
        print(f"You win and you guessed this number in {times} times")
        flag = "fly"

