# Task: Write a program to count of the specified element in an array. 

def count(input_array, character):
    # Add your code here
    sum = 0
    for i in input_array:
        if i == character:
            sum += 1
    return sum
 

# DO NOT EDIT THE CODE BELOW
# Test Cases
arr1=[3, 'a', 'a', 'a', 2, 3, 'a', 3, 'a', 2, 4, 9, 3]
print(count(arr1, 'a'))
print(count(arr1, 2))

# Expected Output: 
# 5
# 2