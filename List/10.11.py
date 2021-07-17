import random
number_list = list(eval(input("enter a no. sep by comma: ")))
print("Not sorted list is: " , number_list )
listcontaingIndex=[]
length = 0
while length<(len(number_list)):
    length = len(listcontaingIndex)
    n = random.randint(0 , len(number_list)-1)
    if n not in listcontaingIndex:
        listcontaingIndex.append(n)
shuffledList =[]
for index in listcontaingIndex:
    shuffledList.append(number_list[index])

print("Shuffled list is " , shuffledList )
