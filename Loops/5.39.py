commision = 0
for m in range(1,13):
    sale = eval(input("enter a value: "))
    if sale<5000 and sale>0:
        Sale = sale*0.08
    elif sale>5000 and sale<10000:
        Sale =  (sale - 5000) * 0.10 + (5000*0.8)
    elif sale>10000:
        Sale =  (sale - 10) * 0.12 + 5000 * 0.10 + 5000 * 0.8
    else:
        print("==invalid entry==")

    commision += Sale
print("Sale is " , commision)


