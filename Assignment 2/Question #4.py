differentValues = []  # this list will contain DIFFERENT NUMBERs
lisT = []
sizeOfList = eval(input("Enter a size of list"))
print("ENTER NUMBER'S")
for i in range(sizeOfList):
    n = eval(input(""))
    lisT.append(n)

length=len(lisT)
for i in range(0, length):
    counter = 0
    for j in range(0, length):
        if lisT[i] == lisT[j]:
            counter+=1
    if counter<=1:
        differentValues.append(lisT[i])
print(differentValues)