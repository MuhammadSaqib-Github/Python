import string
print("   ",end="")
for i in range(1,10):
    print( format( i , "4d")  ,end="")
print()
print("=======================================")
for i in range(1, 10):
    print(i, "|", end="")
    for j in range(1,10):
        print(format(i * j  , "4d") , end="")
    print()

