print("========================================")
for i in range(1, 8):
    for j in range(1, 30):
        if ((i == 1 or i == 7) and (j > 1 and j < 5)):
            if i == 7 and j == 4:
                print("* ", end="")
            else:
                print("* ", end="")
        elif (i == 4) and (j > 1 and j < 5):
            if j == 4:
                print("*", end="")
            else:
                print("* ", end="")

        elif (i == 1 or i == 4) and (j > 6 and j < 10):
            print("* ", end="")

        elif (i == 4) and (j == 7):
            print("*", end="")
        elif (i == 4) and (j == 11):
            print("*", end="")
        elif (i == 2 or i == 3) and (j == 1):
            print("* ", end="")
        elif (i == 5 or i == 6) and (j == 5):
            print("  *", end="")
        elif (i == 1) and (j > 6 and j < 10):
            if (j == 10):
                print("*", end="")
            else:
                print("* ", end="")
        elif (i == 2 or i == 3) and (j == 8):
            print("*", end="")
        elif (i == 2 or i == 3) and (j == 11):
            print("   *", end="")
        elif (i == 5 or i == 6 or i == 7) and (j == 7):
            print("*", end="")
        elif (i == 5 or i == 6 or i == 7) and (j == 11):
            print("  *", end="")

        elif ((i >= 1 and i <= 7) and (j == 12)):
            print(" ", end="")

        elif (i == 1) and (j == 13 or j == 14 or j == 15):
            print("* ", end="")
        elif (i == 6) and (j == 13 or j == 14 or j == 15):
            print(" *", end="")
        elif (i > 1 and i < 6) and (j == 13):
            print("*", end="")
        elif i == 7 and j == 17:
            print("  * ", end="")

        elif (i > 1 and i < 6) and (j == 18):
            print(" *", end="")

        elif ((i >= 1 and i <= 7) and (j == 18)):
            print(" ", end="")

        elif (i >= 2 and i <= 6) and j == 23:
            print("*", end="  ")
        elif (i == 1) and (j >= 19 and j <= 23):
            print("*", end="")
        elif (i == 7) and (j >= 19 and j <= 23):
            print("*", end="")

        elif ((i >= 1 and i <= 7) and (j == 24)):
            print(" ", end="*")
        elif (i == 1 or i == 4 or i == 7) and (j == 26 or j == 27 or j == 28):
            print("* ", end="")
        elif (i == 2 or i == 3 or i == 5 or i == 6) and (j == 29):
            print("  *", end="")

        else:
            if (i == 5 or i == 6) and j == 5:
                print(end="")
            elif (i == 7) and j == 5:
                print(end="")
            elif (i == 4 and j == 10):
                print(end="")
            elif i == 1 and (j == 11):
                print(end="")
            elif i == 1 and (j == 18):
                print(end="")
            elif i == 6 and (j == 18):
                print(end="")
            elif i == 6 and (j == 16):
                print(end="")
            elif i == 6 and (j == 17):
                print(end="")
            elif i == 1 and (j == 16):
                print(end="")
            else:
                print(end=" ")
    print()
print("========================================")
