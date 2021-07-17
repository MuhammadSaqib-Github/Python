for i in range(1, 7):
    for j in range(1,8):
        if(i==1 ) and (j==2 or j==3 or j==5 or j==6 ):
            print("*" , end="")
        elif(i==2 ) and (j==1 or j==4 or j==7):
            print("*" , end="")
        elif(i==3 ) and (j==1 or j==7):
            print("*" , end="")
        elif(i==4) and (j==2 or j==6):
            print("*" , end="")
        elif(i==5) and (j==3 or j==5):
            print("*" , end="")
        elif(i==6) and (j==4):
            print("*" , end="")
        else:
            print(end=" ")
    print()
