integers = eval(input("Enter numbers sep by commas"))
rep = []
for i in range(len(integers)):
    time = 0
    skip="yes"
    for j in range(len(rep)):
        if rep[j]==integers[i]:
            skip="no"
    if skip=="yes":
        c = integers.count(integers[i])
        print(integers[i] , "occued" ,c ,"time")
        rep.append(integers[i])

'''
l = []
r = []
c = 0
index = []
for i in range(7):
    n = eval(input("Enter a number: "))
    l.append(n)
repeated = []
for i in range(len(l)):
    c = 0
    for j in range(len(l)):
        if l[i] == l[j]:
            c = c + 1
    if c <= 1:
        r.append(l[i])
    if c > 1:
        repeated.append(l[i])
        index.append(c)

for i in range(len(r)):
    print(r[i], "occured 1 time")

rep = []
for i in repeated:
    if i not in rep:
        rep.append(i)
ind = []
for i in index:
    if i not in ind:
        ind.append(i)

for i in range(len(ind)):
    print(rep[i], "occured", ind[i], "times")
'''