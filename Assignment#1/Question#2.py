'''
*       (Convert pounds into kilograms) Write a program that converts pounds into kilograms.
*        The program prompts the user to enter a number in pounds, converts it
*       to kilograms, and displays the result. One pound is 0.454 kilograms.
'''

value_in_pounds = eval(input("enter a value in pounds: "))
value_in_kgs =  value_in_pounds * 0.454
print( value_in_pounds , " pounds  is " , value_in_kgs , "kilograms")