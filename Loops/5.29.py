n=2001
i = 0
while n<=2100:
    if n%4==0:
        print(format( n , "5d") , end="")
        i = i + 1
        if i%10==0:
            print()
    n = n + 1
