def SUM(x):
    Sum = 0
    for i in range(1,x+1):
        Sum = Sum + (i/(i+1))
    print("Sum is, " , Sum )

def print_series(x):
    Sum = 0
    for i in range(1, x + 1):
        Sum = Sum + (i / (i + 1))
        print(i , "     " , Sum)


def main():
    i = eval(input("Enter a Range: "))
    SUM(i)
    print_series(i)

main()