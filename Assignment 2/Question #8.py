count = 1
def isPrime(n):
    i = 2
    while i < n:
        if n % i == 0:
            return False
        i = i + 1
    return True
def palindrome(n):
    N=n
    r=0
    while n>0:
        digit = n % 10
        r = (r*10) + digit
        n = n // 10
    if N==r:
        return True
    else:
        return False

def printing(n):
    global count
    if isPrime(n)==True and palindrome(n)==True:
        print(format(n, "8d"), end=" ")
        if count % 10 == 0:
            print()
        count = count + 1

def main():
    n=2
    while count<=100:
        printing(n)
        n+=1
main()