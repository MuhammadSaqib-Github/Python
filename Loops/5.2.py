import random , time
'''
(Repeat additions) Listing 5.4, SubtractionQuizLoop.py, generates five random
subtraction questions. Revise the program to generate ten random addition questions for two integers between
 1 and 15. Display the correct count and test time
'''

add=0
sub=0
count=0

start_time = time.time()
print("Enter no of qusestions for subtraction ")
number_of_sub = eval(input())
print("Enter no of qusestions for ADDITION ")
number_of_add = eval(input())

while add < number_of_add:
    a = random.randint(1,15)
    b = random.randint(1,15)
    print("Sum of " , a , " and " , b , "is? : ")
    num = eval(input())
    if num == a+b:
        count+=1
        print("true")
    else:
        print("false")
    add+=1
print("correct count is " , count)

while sub < number_of_sub:
    a = random.randint(1,15)
    b = random.randint(1,15)
    print("Subtraction  of " , b , " from " , a , "is? : ")
    num = eval(input())
    if num == a-b:
        count += 1
        print("true")
    else:
        print("false")
    sub+=1
print("correct count is " , count)
endtime = time.time()
print("time is " , int(endtime-start_time) , "seconds")

