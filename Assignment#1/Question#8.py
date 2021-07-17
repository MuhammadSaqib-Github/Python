'''
Write a program that prompts the user to enter a point (x, y)
and checks whether the point is within the circle centered at
(0, 0) with radius 10
'''

import math
x,y = eval(input("enter point values"))
distace = math.sqrt(x*x + y*y ) #(x*x + y*y) we can use directly this because one point is (0,0)
if distace<10:
    print("point ( " ,x , y , ") lies inside the circle")
elif distace > 10:
        print("point ( " , x, y, ") lies outside the circle")
else:
    print("point (" , x, y, ") concides with boundary of the circle")

