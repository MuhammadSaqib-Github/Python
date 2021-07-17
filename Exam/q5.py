possible_credits = [0, 20, 40, 60, 80, 100, 120]


Progresses = []  
Trailer = []
Retriever = []
Excluded = []


def the_result(Pass, defer, fail):
    
    if 119 < Pass < 121:
        print("Progress")
        Progresses.append(1)
    elif 100 == Pass:
        print("Progress  (module trailer)")
        Trailer.append(1)
    elif 60 == Pass or 80 == Pass:
        print("Do not Progress - module retriever")
        Retriever.append(1)
    elif fail >= 80:
        print("Exclude")
        Excluded.append(1)
    else:
        print("Do not Progress - module retriever")
        Retriever.append(1)


def pass_thing():
    while True:
        try:
            Pass = int(input("Please Enter the Pass credit:"))  # user will be asked to enter pass credit here
        except ValueError:
            print(
                'Integers required')  # This is to make sure the system displays "integers required" if the user enters anything other than numbers.

        else:
            return Pass


def fail_thing():
    while True:
        try:
            fail = int(input("Now please enter the fail credits:"))

        except ValueError:
            print("Integers required")
        else:
            return fail


def defer_thing():
    while True:
        try:
            defer = int(input("Now please enter the defer credits:"))

        except ValueError:
            print("Integers required")
        else:
            return defer


def histogram():
    print('Progresses', len(Progresses), ':')
    for i in Progresses:
        print('*', end=" ")
    print('\n''Trailer', len(Trailer), ':')
    for i in Trailer:
        print('*', end=" ")
    print('\n''Retriever', len(Retriever), ':')
    for i in Retriever:
        print('*', end=" ")
    print('\n''Excluded', len(Excluded), ':')
    for i in Excluded:
        print('*', end=" ") 


def user_input():
    decision = str(input(
        "Please enter y if you would like to continue or enter q if you want to quit:"))  # This was for histogram where when the user enters q it would print out the histogram before ending the program.
    if decision == "Y" or "y":
        print("Please enter the credits for pass, defer and fail")

        Pass = pass_thing()
        while Pass not in possible_credits:  # This is to make sure the system only accepts 0,20,40,60,80,100 and 120.
            print("Out of range, enter the pass credits again")
            Pass = pass_thing()
            break

        defer = defer_thing()
        while defer not in possible_credits:
            print("Out of range, enter the defer credits again")
            defer = defer_thing()
            break

        fail = fail_thing()
        while fail not in possible_credits:
            print("Out of range, enter the fail credits again")
            fail = fail_thing()
            break

        if Pass + defer + fail != 120:  # This is to make sure if the total is not 120 then dispay the
            # total incorrect total message. Then it would ask the user to enter the credits again.
            print("Total Incorrect")
        else:
            print(the_result(Pass, defer, fail))
            user_input()
    elif decision == "Q" or "q":  # This is to end the program.
        print("The program has ended")
        histogram()
    else:
        print("You can only enter capital y or capital q!")
        user_input()


if __name__ == '__main__':
    user_input()