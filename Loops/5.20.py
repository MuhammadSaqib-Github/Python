rows = eval(input("Enter number of rows"))
columns = eval(input("Enter number of rows"))

print("Pattern basic ")
for i in range(rows ):
    for j in range(columns):
        if j==columns - 1:
            print("*")
        else:
            print("*" , end=" ")


print("Pattern A ")

for i in range(1,rows+1):
    for j in range(1,i+1):
        if(j==i):
            print("*")
        else:
            print("*" , end=" ")


print("Pattern B ")
for i in range(rows,0,-1):
    for j in range(1,i+1):
        if (j == i):
            print("*")
        else:
            print("*", end=" ")

print("Pattern C ")
n=rows
for i in range(1, rows+1):
    for k in range(1,n):
        print(" " , end="")
    n = n - 1

    for j in range(1, i + 1):
        if i==j:
            print("*")
        else:
            print("*" , end=" ")


print("Pattern D ")
n=1
for i in range(rows , 0 , -1):

    for k in range(1,n):
        print("  " , end="")
    n = n + 1

    for j in range(1, i + 1):
        if i==j:
            print("*")
        else:
            print("*" , end=" ")

