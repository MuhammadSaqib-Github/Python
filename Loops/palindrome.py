name = input("enter a word")
length = len(name) - 1
i = 0
while i < length:
    if (name[i] == name[length]):  # i==0 ,length==4
        i += 1
        length -= 1
        if (i == length):
            print("it is palindrome")
            break
        else:
            continue
    else:
        print("palindrome")
        break



