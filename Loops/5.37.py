import math
s = 0
for i in range(1,625):
    s = s + (1/(math.sqrt(i) + math.sqrt(i+1)))
print("Sum is " , s)