# Fibonacci Series
# 0 1 1 2 3 5 8 13 21 34

def fibonacci_series(num):
    f_num = 0
    s_num = 1
    if num == 1:
        print(f_num)
    elif num == 2:
        print(s_num)
    else:
        print(f_num,s_num,sep=" ",end=" ")
        for i in range(num-2):
            t_num = f_num + s_num
            f_num,s_num = s_num,t_num
            print(t_num,end=" ")
num = int(input("Enter a number upto which you want to expand your fibonacci series --> "))
fibonacci_series(num)
