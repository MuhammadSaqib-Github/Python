head = 0
tail = 0
import random
for i in range(1,10000000):
    val = random.randint(0,1)
    if val==0:
        head = head + 1
    else:
        tail = tail + 1

print("Head occured " ,  head , "times")
print("Tail occured " ,   tail , "times")