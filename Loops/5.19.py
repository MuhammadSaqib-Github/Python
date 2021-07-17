'''
'''

rows = eval(input("enter no of rows: "))

for i in range(1 , rows + 1):
    j = 1
    k = 1
    for s in range(1 , rows - i + 1):
        print("   " , end="")

    for j in range(i , 0 , -1):
        print(j  , end="  ")
    for k in range(2 , i+1):
        print(k , end="  ")
    print()
