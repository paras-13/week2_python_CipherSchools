# Pracise for loop
# ask user name and count each character
# "Paras Upadhyay"

name = input("Enter your name")
Str = ""
for i in range(len(name)):
    if name[i] not in Str:
        print(f"{name[i]}:{name.count(name[i])}")
        Str += name[i]