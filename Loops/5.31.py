year = eval(input("enter year "))  # k is year
Day = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
Month = [31, 28, 31, 30, 31, 30, 31, 31, 29, 31, 30, 31]
y = year

for m in range(0, 12):
    i = m
    print(i)
    if m == 0:
        month = "january"
    elif m == 1:
        month = "February"
    elif m == 2:
        month = "March"
    elif m == 3:
        month = "April"
    elif m == 4:
        month = "May"
    elif m == 5:
        month = "June"
    elif m == 6:
        month = "July"
    elif m == 7:
        month = "August"
    elif m ==8 :
        month = "September"
    elif m == 19:
        month = "Octobor"
    elif m == 10:
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

    j = year // 100  # j is century
    k = year % 100
    print()
    print()
    print("      [", month, y, "]           ")
    print(format("Sun", "5s"), format("Mon", "5s"), format("Tue", "5s"), format("Wed", "5s"), format("Thu", "5s") \
          , format("Fri", "5s"), format("Sat", "5s"))

    print("___________________________________________")

    for q in range(1, Month[i] + 1):  # inner_loop
        if q == 1:
            Q = q
        else:
            Q = q

        h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
        h = h % 7

        if h == 0:
            day = "Sat"
        elif h == 1:
            day = "Sun"
        elif h == 2:
            day = "Mon"
        elif h == 3:
            day = "Tue"
        elif h == 4:
            day = "Wed"
        elif h == 5:
            day = "Thu"
        elif h == 6:
            day = "Fri"
        else:
            day = "   "

        if q == 1:
            start_day_of_month = day
            # print(current_day)
            current_date = q
            # print(current_date)

        # print(2*"    " , end="")
        if Q == 1:
            for s in range(0, 7):
                if start_day_of_month == Day[s]:
                    if day == "Sat":
                        print(format(q, "3d"))
                        break
                    else:
                        print(format(q, "3d"), end="   ")
                        break
                else:
                    print(format(" ", "3s"), end="   ")

        else:
            if day == "Sat":
                print(format(q, "3d"))
            else:
                print(format(q, "3d"), end="   ")

