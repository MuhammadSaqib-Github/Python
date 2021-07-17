lisT = [1 ,2 ,2 ,2 ,2 ,1 ,3 ,1 ,3 ,3 ,3 ,1 ,5 ,5  ,5 ,0 ]
occurence = 0
length = len(lisT)
for i in range(length):
    counter=0
    x=i
    for j in range(length):
        y=j
        if (lisT[i]==lisT[j]):
            if y-x==0 or y-x==1:
                counter=counter+1
                x+=1
                y+=1
    if occurence<counter:
        occurence= counter
        word = lisT[i]
print("word is " , word , "and occured " , occurence ,  "times")