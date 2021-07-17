def pentagonal_number(N):
    n_per_line = 10
    for i in range(1,N+1):
        val = int(( i * (3*i - 1 )) / 2)
        print( format(val , "10d") , end="")
        if i%n_per_line == 0:
            print()

def main():
    print("how many number you want to convert into pentagon? ")
    n = eval(input())
    pentagonal_number(n)

main()