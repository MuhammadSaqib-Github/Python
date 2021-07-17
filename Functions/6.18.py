import random
def printMatrix(n):
    i = random.randint(0,1)
    for j in range(1,n+1):
        for j in range(1, n + 1):
            N = random.randint(0, 1)
            if j==n:
                print(N)
            else:
                print(N , end=" ")
def main():
    n = eval(input(" Enter order like ? x ? : "))
    printMatrix(n)
main()