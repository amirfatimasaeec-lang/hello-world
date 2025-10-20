# Snippet 2 - Corrected

def findTotal(a):
  # Added a colon ":" to the end of the for loop statement
  for i in a:
    # Indented this line to place it inside the for loop
    print(sum(i) * 2)

# --- Example of how to run the function ---
# This part is just to show you how it works.
# 'a' needs to be a list of lists, like this:
test_data = [[1, 2, 3], [4, 5, 6], [10, 20]]

# Now, we call the function with our test data
findTotal(test_data)