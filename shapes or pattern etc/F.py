for i in range(1,8):
    for j in range(1,6):
        if i==4 or i==1:
            print("* " , end="")
        elif j==1 and i>=1 and i<=7:
            print("* ", end="")
        else:
            print(end="  ")
    print()