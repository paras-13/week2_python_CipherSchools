# Chapter4 Exercise2

# Program to check whether a string entered by the user is pallindrom or not

def pallindrom(str1):
    if str1 == str1[::-1]:
        return True
    return False

str1 = input("Enter a string to check whether it is pallindrom or not --> ")
print("String provided by the user is a pallindrom --> ",pallindrom(str1))