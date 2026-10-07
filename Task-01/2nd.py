cost_price = int(input("Enter the cost price: "))
selling_price = int(input("Enter the selling price: "))

profit = selling_price - cost_price

if profit > 0:
    print("It's Profit")
elif profit < 0:
    print("It's Loss")
else:
    print("No Profit, No Loss")
