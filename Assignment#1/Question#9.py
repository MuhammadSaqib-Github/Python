'''
Write a program that prompts the user to enter a three-digit integer and determines
whether it is a palindrome number. A number is a palindrome if it reads the same from
right to left and from left to right
'''

number = eval(input("enter a three-digit integer: "))
length = len(str(number))
d3 = number % 10
number //= 10
d2 = number % 10
number //= 10
d1 = number % 10

if length==3:
    if d1==d3:
        print("digit is palindrome")
    elif length != "3":
        print("The numeric value you entered is not 3 digit,so it is not palidrome ")
    else:
        print("Not palindrome")
else:
    print("Not palindrome")
