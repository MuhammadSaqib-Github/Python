loan_amount = eval(input("enter amount"))
year        = eval(input("enter no. of year"))
Total       = loan_amount
loan_amount = loan_amount * (loan_amount * (loan_amount * 1/8) )

print(format("interest rate" , '20s'),  format("Monthly Payment " , '20s') , 'Total payment')
Monthly_rate = float(5.0)

for i in range(5.0 , 8.0):
    annualInterestRate = annualInterestRate + (.125)
