n = 2
print()
while n<10000:
    Sum = 1
    for i in range(2,n):
        if i<n:
            if(n%i==0):
                Sum = Sum + i
    if(Sum==n):
        print(n,end="      ")
    n = n + 1