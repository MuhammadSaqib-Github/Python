r = eval(input("Enter range"))
sum = 0
for n in range(1 , r+1):
    fact = 1
    i=1
    while i<=n:
            fact = fact * i
            i = i + 1
    sum = sum + (1/fact)
print("sum is " , sum + 1)
