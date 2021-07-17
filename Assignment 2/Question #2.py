# by using LISTING
numbers = eval(input("Enter 3 integers sep by commas"))
l = len(numbers)
Occ=0
for i in range(l):
    occ=0
    for j in range(l):
        if numbers[i]==numbers[j]:
            occ+=1
            if occ>Occ:
                Occ = occ

if Occ==1:
    Occ=0 #cuz occurence cant be 1 all are differnt NO number is matched
print("Occurence is ," , Occ)

#Without LISTING
'''
integer1 , integer2 , integer3 = eval(input("enter 1st integer "))
rep = 0
if integer1==integer2 and integer2==integer3 :
    rep=3
elif integer1==integer2 or integer1==integer3 or integer2==integer3:
    rep=2
else:
    rep=rep
print("Input was " , integer1 , integer2 , integer3)
print("Output is " , rep  )
'''

