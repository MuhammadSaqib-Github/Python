import random
n1 =  random.randint(0,99)
n2 =  random.randint(0,n1)

while n1!=n2:
    n2 = random.randint(0, n1)
print(f"Now {n1} and {n2} are same")