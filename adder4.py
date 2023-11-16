# Generalizing the function to take an arbitrary number of keyword arguments

def adder_arbitrary_keywords(**kwargs):
    return sum(kwargs.values())


# Calling the function with arbitrary keyword arguments
result_arbitrary_keywords = adder_arbitrary_keywords(ugly=10, good=5.3, bad=2.9)
print("Arbitrary Keyword result:", result_arbitrary_keywords)
