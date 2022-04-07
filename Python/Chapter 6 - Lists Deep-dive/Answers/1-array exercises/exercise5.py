# Task: Write a Python function to find an array contains a specific element.
# Hint: You should leverage the "item in list function"
# Reference: https://appdividend.com/2020/01/21/python-list-contains-how-to-check-if-item-exists-in-list

def contains(array, target):
    # Add your code here
    return target in array



# DO NOT EDIT CODE BELOW
# Test Case
arr = [2, 5, 9, 6]
print(contains(arr, 5))
print(contains(arr, 1))

# Expected Output
# True
# False