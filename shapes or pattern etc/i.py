for i in range(1,8):
    for j in range(1,6):
        if i==1 or i==7:
            print("* " , end="")
        elif j==3 and i>1 and i<7:
            print("* ", end="")
        elif i==1 or i==7:
            print("* " , end="")
        elif j==3 and i>1 and i<7:
            print("* ", end="")
        else:
            print(end="  ")
    print()