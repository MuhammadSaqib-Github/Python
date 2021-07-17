import random
lisT = [0,1, 2, 3, 4, 5, 6, 7, 8, 9]
occ = [0, 0, 0, 0, 0, 0, 0, 0, 0,0]
for i in range(100):
    n = random.randint(0, 9)
    for j in range(len(lisT)):
        if lisT[j] == n:
            occ[j] = occ[j] + 1
            break
for i in range(10):
    print(lisT[i], "randomly occured", occ[i])