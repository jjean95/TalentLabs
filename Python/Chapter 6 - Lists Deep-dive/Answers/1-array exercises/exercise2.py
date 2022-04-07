# Task: Write a Python function to get the first 'n' elements of an array.
# Passing a parameter 'n' will return the first 'n' elements of the array.
# Hint: You can create an empty list first, then add the first n elements to the list, and return it at the end of the function

def first(input_array, number_of_elements):
    # Add your code here
    list2 = []
    list2.append(input_array[:number_of_elements])
    return list2

# DO NOT EDIT CODE BELOW
# Test Cases :
print(first([7, 9, 0, -2],3))
print(first([7, 9, 0, -2, 9 ],4))


# Expected Results
# [7, 9, 0]
# [7, 9, 0, -2]