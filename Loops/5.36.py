
win  = 0
import random
while win<2:
    print(win)
    n = random.randint(0, 2)
    print("n=" , n )
    turn = eval(input("scissor (0), rock (1), paper (2): "))
    print("turn=" , turn)
    if turn==n:
        print("computer and you are same, draw")
    elif turn==0 and n==2:
        print("computer is scissor and you are paper too, you won")
        win += 1
    elif turn==1 and n==0:
        print("computer is scissor and you are rock too, you won")
        win += 1
    elif turn==2 and n==1:
        print("computer is rock and you are paper too, you won")
        win += 1
    else:
        print("better luck next time")
print("You won 2 times")

