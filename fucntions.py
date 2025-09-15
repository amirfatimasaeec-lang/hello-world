# Function to calculate area of a circle
def area_circle(pi, radius):
    return pi * (radius ** 2)

# Function to calculate total due with tax
def total_due(money, tax_rate):
    return money + (money * tax_rate)

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * (5 / 9)


# -------- Main Program --------
pi = 3.1416

# Circle Area
radius = float(input("Enter radius of the circle: "))
circle_area = area_circle(pi, radius)
print("Area of Circle:", round(circle_area, 2))
print()

# Taxes
money = float(input("Enter money amount: "))
tax_rate = float(input("Enter tax rate (as %, e.g. 6 for 6%): ")) / 100
due = total_due(money, tax_rate)
print("Total Due:", round(due, 2))
print()

# Temperature
fahrenheit = float(input("Enter temperature in Fahrenheit: "))
celsius = fahrenheit_to_celsius(fahrenheit)
print("Celsius:", round(celsius, 5))

