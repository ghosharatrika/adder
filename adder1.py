# Defining the adder function to add two numbers
def adder(a, b):
    return a + b


# Call the function to add two strings, two lists, and two floating points
result_string = adder("Hello ", "World!")
result_list = adder([1, 2, 3], [4, 5, 6])
result_float = adder(35.97, 10.987)

# Print the results
print("String result:", result_string)
print("List result:", result_list)
print("Float result:", result_float)
