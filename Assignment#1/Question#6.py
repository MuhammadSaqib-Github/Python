'''
Write a program that prompts the user to enter three integers and displays them in
increasing order.
'''

number1 = eval(input("enter 1st number"))
number2 = eval(input("enter 2nd number"))
number3 = eval(input("enter 3rd number"))

if(number2 < number1 or number3 < number1):
    if(number1>number2):
        number1 , number2 = number2 , number1       #swap of values
    if(number1>number3):
        number1 , number3 = number3 , number1       #swap of values
    if(number2>number3):
        number3 , number2 = number2 , number3       #swap of values

print("Sorted values are: "number1 ,"  ", number2,"   " , number3)

