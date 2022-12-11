# To make a number guessing game

from random import randint as r
r_num = r(0,100)
flag = "down"
times = 0
u_num = int(input("Guess a number between 0 and 100 : "))
while flag == "down":
    if u_num == r_num:
        times +=1
        print(f"You win and you guessed this number in {times} times")
        flag = "fly"
    else:
        if u_num < r_num:
            print("Too low")
        else:
            print("Too high")
        times +=1
        u_num = int(input("Guess Again : "))
        flag = "down"
        
