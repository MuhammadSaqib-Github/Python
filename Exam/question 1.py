import math
choice = eval(input("Enter how many times you want to enter values of x and y co-ordinates: "))
list1=[]
list2=[]
for i in range(choice):
    
    x1,y1=eval(input("Enter the values of x1 and y1 co-ordinates: "))
    x2,y2=eval(input("Enter the values of x2 and y2 co-ordinates:"))
    list1.append(x1)
    list1.append(y1)
    list2.append(x2)
    list2.append(y2)
    d = math.sqrt((x2-x1)**2 + (y2-y1)**2)
    a=str(d)
    c=a
if list1>list2:
    print("Two points having maximum distance are ",(x1,y1),(x2,y2),".The distance is ",c )
    
else:
    print("Two points having maximum distance are ",(x1,y1),(x2,y2),".The distance is ",c )