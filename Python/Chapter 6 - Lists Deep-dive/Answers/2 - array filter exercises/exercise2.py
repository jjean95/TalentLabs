# Task: Given an array of numbers, return a new array that only includes the even numbers.

def evens_only(arr):
  # Add your code here
  new_arr = []
  for i in arr:
    if i % 2 == 0:
      new_arr.append(i)
  return new_arr

# DO NOT EDIT CODE BELOW
# Test Case
print(evens_only([3, 2, 8, 9, 11])) 

# Expected Output
# [2, 8]
  