l = eval(input("enter numbers sep by commas: "))
reverse = []
for i in range(len(l) - 1, -1 , -1):
    reverse.append(l[i])
print(reverse)