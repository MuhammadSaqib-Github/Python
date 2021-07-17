import math
i = eval(input("enter range: ")))
Sum = 0
for j in range(1,i+1):
    Sum = Sum + (math.pow((-1),(j + 1)))/(2*j - 1)
print("Sum is :" , 4*Sum)
