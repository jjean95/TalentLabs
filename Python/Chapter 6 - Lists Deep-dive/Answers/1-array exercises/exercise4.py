# Task: Write a Python function to remove a specific element from an array.
# You can assume that there are 1 and only 1 existence of the target in the array
# Hint: You might want to check the documentation of array.remove() function

def remove_array_element(array, target):
    # Add your code here
    return array.remove(target)




# DO NOT EDIT CODE BELOW
# Test Case
array1 = [2, 5, 9, 6]
remove_array_element(array1, 5)
print(array1)

# Expected Output
# [2, 9, 6]