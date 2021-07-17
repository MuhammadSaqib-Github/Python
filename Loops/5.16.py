n1,n2 = eval(input("Enter values "))
n=1
if(n1>n2):
    n = n2
    while True:
        if(n1%n==0  and n2%n==0):
            print("GCD is " ,  n)
            break
        n = n -1
else:
    n = n1
    while True:
        if(n1%n==0  and n2%n==0):
            print("GCD is " ,  n)
            break
        n = n -1