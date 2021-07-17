dayInWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
EmployeeHours = []

noOfEmployee = eval(input("Enter a no. of  Employess"))
for i in range(noOfEmployee):
    n = []
    n = eval(input("Enter the working hours separated by commas from Su to Sa for employee " + str(i) + ": "))
    EmployeeHours.append(n)


def displayEmployee(record):
    global dayInWeek, EmployeeHours, noOfEmployee
    print("          ", end=" ")
    for day in record[0]:
        print(format(day, "4s"), end="")
    print()

    for i in range(noOfEmployee):
        print("Employee", i, end=" ")
        for j in range(7):
            print(format(record[1][i][j], "3d"), end=" ")
        print()
    print()


def totalHours(record):
    Employee = []
    global dayInWeek, EmployeeHours
    for rec in record[1]:
        Sum = 0
        for i in rec:
            Sum = Sum + i
        Employee.append(Sum)
    return Employee


def decreasingOrder(hours):
    global noOfEmployee
    x = 0
    l = []
    dec = []
    current = []
    for i in range(noOfEmployee):
        l.append(i)
    for i in range(noOfEmployee):
        current.append(hours[i])

    for i in range(len(hours) - 1):
        for j in range(i + 1, len(hours)):
            if hours[i] < hours[j]:
                hours[i], hours[j] = hours[j], hours[i]
                l[i], l[j] = l[j], l[i]
    print(hours)
    dec = hours
    print("Record in decreasing order is :")
    print(dec)
    for i in range(noOfEmployee):
        for j in range(noOfEmployee):
            if dec[i] == current[j]:
                print("Employees ", l[i], "hours are", hours[i])
                break

def main():
    hours = []
    decOrder = []
    global dayInWeek, EmployeeHours
    record = [dayInWeek, EmployeeHours]
    displayEmployee(record)
    hours = totalHours(record)
    print("According to input, worked hours order is ")
    print(hours)
    print()
    decreasingOrder(hours)
main()