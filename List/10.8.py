def main():
    lst = eval(input("Enter no.s sep by commas"))
    m=indexOfSmallestElement(lst)
    print("SMALLEST INDEX IS " , m)

def indexOfSmallestElement(lst):
    Min=0
    minval = lst[0]
    for i in range(1,len(lst)):
        if minval>lst[i]:
            Min=i
    return Min

main()