def rev(l):
    r=[]
    for i in range(0,len(l)):
        r.append(l[ len(l)-1-i])

    return r

lst = list(eval(input("enter a numbers sep by comma: ")))
print(type(lst))
r = rev(lst)
print(r)

