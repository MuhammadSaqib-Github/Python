uni_fee = 10000
year = 1
cost = 0
while year < 15:
    uni_fee = uni_fee + (uni_fee * 0.05)
    year+=1
    if year == 10:
        print("Fee after 10 year is ", int(uni_fee))
        cost = uni_fee
    if year > 10 and year < 15:
        if year==11:
            uni_fee = uni_fee - cost
            print("11th year fee is " , uni_fee )
            cost1 = uni_fee
        cost1 = cost1 + (cost*0.05)
print("cost is  ", int(cost1))