count = 0
for i in range(1,8):
    for j in range(1,8):
        if i==j or j<i:
            continue
        else:
            print(i , j)
            count = count + 1

print("count is " , count)

