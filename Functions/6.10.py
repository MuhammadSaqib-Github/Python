count = 1
def printing(n):
    global count
    if isPrime(n):
        print(format(n, "3d"), end=" ")
        if count % 10 == 0:
            print()
        count = count + 1

def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True

def main():
    for n in range(2, 1000):
        printing(n)

main()
