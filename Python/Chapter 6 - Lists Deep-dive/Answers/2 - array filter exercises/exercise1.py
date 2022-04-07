# Task: Given an array of numbers, return a new array that has only the numbers that are 10 or greater.

def ten_and_greater_only(arr):
  # Add your code here
  new_list = []
  for num in arr:
    if num >= 10:
      new_list.append(num)
  return new_list

# DO NOT EDIT CODE BELOW
# Test Case
print(ten_and_greater_only([10, 2, 3, 8, 4, 13, 22]))

# Expected Output
# [10, 13, 22]