l = input()
item = []
skip = "yes"
for c in l:
    if c ==" ":
        skip = "no"
    else:
        skip = "yes"

    if skip == "yes":
        item.append(int(c))
distinctNumbers = []
for i in item:
    if i not in distinctNumbers:
        distinctNumbers.append(i)
print("Distinct values are: ", distinctNumbers)