# snippet1.py
# Debugged and corrected version

# Open (or create) the file 'output.txt' in append mode
db = open("output.txt", "a")

# Fixed the type error by making both parts strings
a = "Hello" + "1"
b = "How do you do?"

# Write the message to the file
db.write(a + ", " + b + "\n")

# Close the file properly
db.close()
