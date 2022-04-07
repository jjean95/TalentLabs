# Task: Write a Python function to merge two arrays
# Hint: You might want to check the documentation of array.extend() function

def merge_array(arr1, arr2):
    # Add your code here
    arr1.extend(arr2)
    

# DO NOT EDIT CODE BELOW
# Test Case :
array1 = [1, 2, 3]
array2 = [2, 30, 1]
merge_array(array1, array2)
print(array1)

# Expected Output
# [1, 2, 3, 2, 30, 1]