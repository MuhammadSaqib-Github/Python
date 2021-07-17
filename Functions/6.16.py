def numberOfDaysInAYear(year):
    print(year)
    if (year%4==0 and year%100!=0) or year:
        print("366 DAYS")
    else:
        print("365 DAYS")

def main():
    for n in range(2010 , 2021):
        numberOfDaysInAYear(n)

main()