year = eval(input("enter year "))
y = year
for m in range(1,13):
    if m == 1:
        month="january"
    elif m == 2:
        month = "February"
    elif m == 3:
        month = "March"
    elif m == 4:
        month = "April"
    elif m == 5:
        month = "May"
    elif m == 6:
        month = "June"
    elif m == 7:
        month = "July"
    elif m == 9:
        month = "September"
    elif m == 10:
        month = "Octobor"
    elif m == 8:
        month = "August"
    elif m == 11:
        month = "November"
    else:
        month = "December"

    year = y
    if m == 1:
        m = 13
        year = year - 1

    elif m == 2:
        m = 14
        year = year - 1
    else:
        m = m

    j = year//100                   #j is century
    k = year % 100
    q = 1
    h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
    h = h % 7

    if h == 0:
        day = "saturday"
    elif h == 1:
        day = "sunday"
    elif h == 2:
        day = "monday"
    elif h == 3:
        day = "tuesday"
    elif h == 4:
         day = "wednesday"
    elif h == 5:
        day = "thursday"
    elif h == 6:
        day = "friday"
    else:
        print("some entered invalid")
    m = 1
    print(month , q , "," , year , "is" , day)