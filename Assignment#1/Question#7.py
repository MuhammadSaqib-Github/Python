'''
(Compute the perimeter of a triangle) Write a program that reads three edges for a
triangle and computes the perimeter if the input is valid. Otherwise, display that the
input is invalid. The input is valid if the sum of every pair of two edges is greater than
the remaining edge.
'''


x1,x2,x3 = eval(input("Enter three edges for a triangle:"))

if (x1+x2 > x3) and (x1+x3 > x2) and (x2+x3 > x1):
    print("Input is Valid , so", end=" ")
    print("Perimeter is: ", x1+x2+x3)
else:
    print("input is invalid")