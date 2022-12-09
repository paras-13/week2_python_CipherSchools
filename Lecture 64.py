# practise for loop
# Ask user a number like 1256
# calculate sum of dihits :--> 1+2+5+6
num = input("Enter a number")
Sum = 0
for i in range(len(num)):
    Sum += int(num[i])
print(Sum)
