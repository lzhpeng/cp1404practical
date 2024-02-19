sales = float(input("Enter your sales:"))
while sales >= 0:
    if sales < 1000:
        bonus = sales * 0.1
    else:
        bonus = sales * 0.15
    print(bonus)
    sales = float(input("Enter your sales:"))