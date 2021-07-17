n, Sum1 = 50000, 0
Sum1 = 0
for i in range(1, n + 1):
    Sum1 = Sum1 + 1 / i

print("Sum1 is ", Sum1)

n, Sum2 = 50000, 0
for i in range(50000, 0, -1):
    Sum2 = Sum2 + 1 / i
print("Sum2 is ", Sum2)
print("after comparing of value difference is " , format(Sum2 - Sum1 , "10.9"))

print(5.9999999999999999999 - 5.999999999999999)