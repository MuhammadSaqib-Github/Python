val = eval(input("Enter a dollar: "))
Sum = 0
mul = (1 + 0.00417)
for m in range(1,13):
    print("After end of," , m , "month" , end=" ")
    Sum = Sum + val
    Sum = Sum*mul
    print("Interest rate is  " , Sum)
