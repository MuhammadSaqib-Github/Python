rows = eval(input("enter value of rows"))

for i in range(1, rows + 1):
    for j in range(1 , rows - i +1):
            print("  " , end="")
    n = 2
    for k in range(1,i + 1):
            if(k==1):
                print(k , end=" ")
            else:
                print( n , end=" " )
                n = n + n
                continue
    n = (n)//4
    for l in range(1 , i ):
            if(l==i-1):
                print( 1 , end=" " )
            else:
                print( n  , end=" " )
                n = n - n//2
                continue
    print()