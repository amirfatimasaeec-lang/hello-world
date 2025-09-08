# Electric Bill Calculator

kwh = int(input("Enter the KW hours used: "))

if kwh <= 1000:
    amount = kwh * 0.07633
else:
    amount = (1000 * 0.07633) + ((kwh - 1000) * 0.09259)

print("Amount owed is $", round(amount, 2))

