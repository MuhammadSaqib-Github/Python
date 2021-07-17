list1= []
while True:
    val1_in_kg = eval(input("enter value in kg"))
    val2_in_pound = eval(input("enter value in pound"))
    val1_in_pound = val1_in_kg * 2.2
    val2_in_kg = val2_in_pound / 2.2
    print("Kilograms  Pounds |   Pounds  Kilograms")
    print(val1_in_kg ,"        " ,val1_in_pound ,"  " , "|" ," "  , val2_in_pound ,"     " , val2_in_kg )
    num =  eval(input("enter 0 to exit or press any key to continue: "))
    if num == 0:
        break