def merge(list1, list2):
    lenOfList1 = len(list1)  # Taking length,cuz i want size to check n0. of values of list1
    lenOfList2 = len(list2)  # Taking length,cuz i want size to check n0. of values of list2
    indexing0fList1 = 0  # index starts from 0 thats why i intialized it with "0"
    indexing0fList2 = 0  # index starts from 0 thats why i intialized it with "0"
    combinedLength = len(list1) + len(list2)  # Taking combined list cuz , it will size of MERGED list
    mergedList = []  # declaring list
    currentLengthOfMergedList = len(mergedList)  # used variable bcuz in mergedlist indexing starts from 0 \
    # current length is  "0"  at start

    while currentLengthOfMergedList < combinedLength:
        if indexing0fList1 < lenOfList1:  # length of list1 is 5 so in this contol will iterarte 5 times
            mergedList.append(list1[indexing0fList1])
            currentLengthOfMergedList += 1
            indexing0fList1 += 1
        if indexing0fList2 < lenOfList2:  # length of list1 is 4 so in this contol will iterarte 5 times
            mergedList.append(list2[indexing0fList2])
            currentLengthOfMergedList += 1
            indexing0fList2 += 1
    sort(mergedList)


def sort(sort_list):
    for i in range(len(sort_list) - 1):  # outerloop
        for j in range(i + 1, len(sort_list)):  # innerloop
            if sort_list[i] > sort_list[j]:
                sort_list[i], sort_list[j] = sort_list[j], sort_list[i]  # swapping
    print("Merged & Sorted list is: ", sort_list)


def main():
    list1 = []
    sizeOfList1 = eval(input("Enter size of list 1"))
    print("Enter values for list1 in Sorted form")
    for i in range(sizeOfList1):
        n = eval(input())

        if i == 0:
            list1.append(n)
        else:
            list1.append(n)
            while True:
                if (list1[i - 1] > list1[i]):
                    list1.pop()
                    print("You entered smaller value than previous value, enter value again ")
                    n = eval(input())
                    list1.append(n)
                    if (list1[i - 1] < list1[i]):
                        break
                else:
                    break

    list2 = []
    sizeOfList2 = eval(input("Enter size of list 2"))
    print("Enter values for list2")
    for i in range(sizeOfList2):
        n = eval(input())
        if i == 0:
            list2.append(n)
        else:
            list2.append(n)
            while True:
                if (list2[i - 1] > list2[i]):
                    list2.pop()
                    print("You entered smaller value than previous value, enter value again ")
                    n = eval(input())
                    list2.append(n)
                    if (list2[i - 1] < list2[i]):
                        break
                else:
                    break

    merge(list1, list2)
main()