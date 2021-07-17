def sort(A):
    Cs=0
    Ss=0
    for i in range(len(A)-1):
        if A[i]>=A[i+1]:
            Cs=0
        else:
            Cs = Cs + 1
            break
        
    for i in range(len(A)-1):
        if A[i]<=A[i+1]:
            Ss=0
        else:
            Ss = Ss + 1
            break
        
    if Ss==0 or Cs==0:
        return "sorted"
    else:
        return "not sorted"
        
def main():
    A=[2,4,5,9,9,11]
    print("List is " , sort(A))    
main()