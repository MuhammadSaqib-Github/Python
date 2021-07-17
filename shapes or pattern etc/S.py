for i in range(1,8):
    for j in range(1,6):
        if (i==1 or i==4 or i==7) and (j>1 and j<5):
            print("* " , end="")
        elif (i==2 or i==3) and (j==1):
            print("*" , end="")
        elif (i==5 or i==6) and (j==5):
            print("*" , end="")
        else:
            print(end="  ")
    print()