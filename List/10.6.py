import math

prime = "yes"
cn = 2
c = 1
r = 0
lst = []
while c <= 50:
    n = 2
    while n <= int(math.sqrt(cn)):
        if cn % n == 0:
            r = r + 1
        n = n + 1
    if r > 0:
        prime = "n0"
    else:
        prime = "yes"
    r = 0
    if prime == "yes":
        lst.append(cn)
        c = c + 1

    cn = cn + 1
for i in range(len(lst)):
    if (i+ 1) % 10 == 0:
        print(format(lst[i], "4d"))
    else:
        print(format(lst[i], "4d"), end="")


