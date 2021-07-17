def grade(test , grade):
        if grade>test - 10:
            return 'A'
        elif grade>test -20:
            return 'B'
        elif grade > test - 30:
            return 'C'
        elif grade > test - 40:
            return 'D'
        else:
            return 'F'
def main():
    l = eval(input("enter numbers: "))
    for i in range(len(l)):
        g = grade(100 , l[i])
        print("Marks are "  , l[i] , " and grade is " , g)
main()