#a*x**2 + b*x + c = 0 which is equation 4 root
#ask user to enter value of a , b , c
import math
a = eval(input("enter value for a"))
b = eval(input("enter value for b"))
c = eval(input("enter value for c"))

disc = b * b - 4 * a * c

if disc<0:
    print("invalid input of values" , end="  ")
    print("there will be no root when discrement is -ve  and no roots for equation")
elif disc>0:
    root1 = (-b + math.sqrt(disc)) / 2 * a
    root2 = (-b - math.sqrt(disc)) / 2 * a
    print("root 1 is " , root1 , " root 2 is " , root2)
else:
    root = -b / 2 * a
    print("since dicremenent is ze2ro so root is ", root )