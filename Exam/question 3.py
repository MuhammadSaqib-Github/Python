def difference(x,y):
    list1=list(x)     
    list2=list(y)
    n=list(list1)     
    for i in range(len(list1)):         
        for j in range(len(list2)):             
            if list1[i]==list2[j]:               
                n.remove(list1[i])
    print("The difference of these two sets is ",n)     
def main():
    set1=set([2,4,6,8,10,11,3])     
    set2=set([1,2,3,4])     
    difference(set1,set2) 
main()