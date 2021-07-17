def Mean(lst):
    m = 0
    for i in range(len(lst)):
        m = m + float(lst[i])
    m=m/len(lst)
    return m

def deviation(lst,m):
    d = 0
    for i in range(len(lst)):
        d = d + ((float(lst[i]) - m)**(0.5))

    d = d/((len(lst) - 1)**(0.5))
    return d

lst = input("Enter numbers sep by commas,,,...? : ")
lst = lst.split()
print(lst)
m= Mean(lst)
print("Mean is " , m)
d=deviation(lst,m)
print("Deviation is " , d)
