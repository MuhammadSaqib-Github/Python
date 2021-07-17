'''
(Sum the digits in an integer) Write a program that reads an integer between 0 and
1000 and adds all the digits in the integer. For example, if an integer is 932, the
sum of all its digits is 14.
Hint: Use the % operator to extract digits, and use the / operator to remove the
extracted digit. For instance, 932 % 10 = 2 and 932 / 10 = 93.
'''

number = eval(input("enter number between 0-1000 :"))
lessThan10 = number % 10	        	# Extract the digit less than 10
number //= 10							# Remove the extracted digit
tens = number % 10				        # Extract the digit between 10 to 99
number //= 10							# Remove the extracted digit
hundreds = number % 10		            # Extract the digit between 100 to 999

sum = hundreds + tens + lessThan10

print("The sum of the digits is " , int(sum))  # Display result