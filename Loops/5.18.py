factors = []
num = eval(input("enter value "))
n=2

while True:
    if num%n==0:
        num = num // n
        factors.append(n)
    if num % n == 0:
        n=2
    else:
        n = n + 1
    if(num==1):
        break
print(factors)

'''
num=int(input("Enter an integer"))
n=2
while num!=n:
    if num%n==0:
        print(n)
        rem=num//n
        num=rem
    else:
        n+=1
print(n)
'''

'''
import math
# A function to print all prime factors of  
# a given number n 
def primeFactors(n): 
      
    # Print the number of two's that divide n 
    while n % 2 == 0: 
        print(2) 
        n = n / 2
          
    # n must be odd at this point 
    # so a skip of 2 ( i = i + 2) can be used 
    for i in range(3,int(math.sqrt(n))+1,2): 
          
        # while i divides n , print i ad divide n 
        while n % i== 0: 
            print(i), 
            n = n / i 
              
    # Condition if n is a prime 
    # number greater than 2 
    if n > 2: 
        print(n)
          
# Driver Program to test above function 
  
n = eval(input("entry "))
primeFactors(n)
'''
