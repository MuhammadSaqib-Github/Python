def printChars(ch1, ch2, numberPerLine):
    count = 1
    while ch1<=ch2:
        print( chr(ch1) , end="  ")
        ch1 = ch1 + 1
        if count % numberPerLine ==0:
            print()
        count = count + 1

def main():
    ch1 = input("Enter starting character: ")
    ch2 = input("Enter ending character: ")
    numberPerLine = eval(input("Enter numbers per line"))
    ch1 = ord(ch1)
    ch2 = ord(ch2)
    printChars(ch1, ch2, numberPerLine)

main()