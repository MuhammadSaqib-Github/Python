for i in range(1,8):
    for j in range(1,6):
        if(j==1):
            print("* "  , end="")
        elif (i==1 or i==4 or i==7) and j>1 and j<5:
            print("* " , end="")
        elif (j==5 and (i==2 or i==3 or i==5 or i==6)):
            print("     *",end="")
        else:
            print(end="")
    print()