def commision(sales):
    if sales <= 5000:
        com = sales * 0.08
    elif sales<=10000:
        com = (sales - 5000 ) * 0.10 + (5000 * 0.08)
    else:
        com = (sales - 10000) * 0.12 + 5000 * 0.10 + 5000 * 0.08
    return com

def main():
    print("Sales Amount         Commision")
    for i in range(10000 , 100001 , 5000 ):
        print(i , "    " , commision(i))

main()