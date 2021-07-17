'''number = eval(input("enter a number "))
pos = 0
neg = 0
total = 0
while number!=0 :
    total = total + (number)
    if number < 0:
        neg+=1
    elif number>0:
        pos += 1
    else:
        print(" you entered 0 ")
    number = eval(input("enter a number "))
else:
    print(" you entered 0 , so control terminated ")
    if pos>0:
        print(f" you entered {pos} times +ve number  ")
    if neg>0:
        print(f" you entered {neg} times +ve number  ")
print("total is " , total)
print("AVG is " , total/(pos+neg))'''


#Alternate way

'''
pos = 0
neg = 0
total = 0
while True:
        number = eval(input("enter a number "))
        if number==0:
            break
        total = total + number
        if number < 0:
            neg += 1
        elif number > 0:
            pos += 1
        else:
            if pos > 0:
                print(f" you entered {pos} times +ve number  ")
            elif neg < 0:
                print(f" you entered {neg} times +ve number  ")
            else:
                 print(" you entered 0 ")

print(" you entered 0 ")
print("total is " , total)
print("AVG is " , total/(pos+neg))
'''



