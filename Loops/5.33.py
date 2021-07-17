val = eval(input("Enter a dollar: "))
n = eval(input("Enter Number of days: "))
yeild = eval(input("Enter %age"))
p = ( yeild / 1200 )
for m in range(1,n+1):
    print("After end of," , m , "month" , end=" ")
    i_amount = val * p
    val = val + i_amount
    print("Interest rate is  " , val)
