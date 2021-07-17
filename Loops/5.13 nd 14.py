n = 0
for i in range(100 , 1000+1):
    if(i%5==0 and i%6==0):
        print(i , end="  ")
        n+=1
        if(n%10==0):
            print()

