n = eval(input("enter range: "))
Sum = 0
for i in range(1,n+1,2):
    Sum= Sum + i/(i+2)
print("Sum is " , Sum)
