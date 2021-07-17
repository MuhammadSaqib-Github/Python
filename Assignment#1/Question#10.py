'''
Write a Python program which accepts a 4 digit binary numbers as its input and check
if the number is even or not.
'''

number = eval(input("Enter 4 digit binary number to check it is even or odd: "))
Number = number
length = len(str(Number))
n1 = number%10                           #To extract last digit
number //= 10
n2 = number%10
number //= 10
n3 = number%10
number //= 10
n4 = number%10

if length!=4:
    print("Not a 4 digit number")
elif n1==0 or n2==0 or n3==0 or n4==0 or n1==1 or n1==1 or n2==1 or n3==1 or n4==1:
    if Number%2==0:
        print("Binary number is EVEN")
    else:
        print("Binary number is ODD")
else:
    print("The number you entered is not Binary")

