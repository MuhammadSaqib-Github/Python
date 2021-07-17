maxX = eval(input("enter a number"))
sec_maxX = eval(input("enter a number"))
count = 1
if maxX > sec_maxX:
    maxX = maxX
    sec_maxX = sec_maxX
else:
    maxX, sec_maxX = sec_maxX, maxX

for i in range(2, 7):
    n = eval(input("enter a number"))
    if (maxX <= n):
        if maxX == sec_maxX:
            sec_maxX = 0
            count = count + 1
        N = sec_maxX
        if maxX != n:
            sec_maxX = maxX
        maxX = n

        if sec_maxX != N:
            count = count - 1

        count = count + 1
        N = sec_maxX

    elif sec_maxX < n:
        sec_maxX = n
    else:
        maxX = maxX
        sec_maxX = sec_maxX

print("Max is ", maxX)
print("2ND Max is ", sec_maxX)
print("Occurrence is ", count)