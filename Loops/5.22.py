v = 0
for n in range(2,1000):
    p = 0
    for i in range(1,n+1):
        if(n%i==0):
            p = p + 1

    if(p==2):
        print(format(n , "5d") , end="")
        v += 1
        if v%10==0:
            print()
    n = n + 1