# Function to return letter grade based on average
def get_letter_grade(avg):
    if avg >= 90:
        return "A"
    elif avg >= 80:
        return "B"
    elif avg >= 70:
        return "C"
    elif avg >= 60:
        return "D"
    else:
        return "F"

# Inputs (no loops)
name = input("Enter the student's name: ")

g1 = int(input("Enter grade 1: "))
g2 = int(input("Enter grade 2: "))
g3 = int(input("Enter grade 3: "))
g4 = int(input("Enter grade 4: "))
g5 = int(input("Enter grade 5: "))

# Use a list (per instructions)
grades = [g1, g2, g3, g4, g5]
average = sum(grades) / 5
# Optional: show the list like in the examples
print(f"List: {grades[0]} {grades[1]} {grades[2]} {grades[3]} {grades[4]}")

# Output format
print("\n" + name)
print(f"\nAverage: {average:g}\n")  # :g avoids trailing .0 (prints 80 instead of 80.0)
print("Letter Grade:", get_letter_grade(average))


