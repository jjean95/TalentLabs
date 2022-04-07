# Write a function to find an array contains a specific element.

def contains(input_list, target):
    # Add your code here
    if target in input_list:
        return True
    else:
        return False  


# DO NOT EDIT THE CODE BELOW
# Test Case
arr = [2, 5, 9, 6]
print(contains(arr, 9))
print(contains(arr, 12))

# Expected Output: 
# True
# False