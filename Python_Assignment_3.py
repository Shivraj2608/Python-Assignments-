# Taking multiple inputs in a single line
# Get multiple inputs in a single line
user_input = input("Enter values separated by spaces: ")

# Split the input string into a list of individual strings
input_list = user_input.split()

# Assign the first three values to variables (assuming at least three values are entered)
if len(input_list) >= 3:
    var1 = input_list[0]
    var2 = input_list[1]
    var3 = input_list[2]

# Print the assigned variables
if len(input_list) >= 3:
    print("Variable 1:", var1)
    print("Variable 2:", var2)
    print("Variable 3:", var3)
else:
    print("Not enough input values provided.")
