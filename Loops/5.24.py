balance =  eval(input("ENTER LOAN AMOUNT"))
no_of_years =  eval(input("ENTER NUMBER OF YEARS"))
interest_rate =  eval(input("ENTER INTEREST RATE in %AGE"))

print(format(Payment" , "20s"), format("Interest" , "20s"), format("Principal" , "20s") ,format("Balance" , "20s"))

monthly_interest = interest_rate/1200
monthly_payment = balance / 12
for i in range(1, no_of_years * 12 + 1):
    interest = monthly_interest * balance
    principal = monthly_interest - interest
    balance = balance - principal
    print( format(i , "15.3f"), format( interest,"15.3f") , format(principal, "15.3f") , format(balance , "15.3f"))
