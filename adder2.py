# Generalization of the adder function to add an arbitrary number of arguments
def adder_general(*args):
    return sum(args)


# Calling the generalized function
result_general = adder_general(0.23, 2.09, 3.14, 4, 5.78, 9.87)
print("\nGeneralized result:", result_general)
