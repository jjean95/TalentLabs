# Task: Print out the array in reverse order (without using array.reverse())

arr = [1, 3, 5, 7, 9, 11, 13]

# Add your code here:
new_arr = 0
i = len(arr) - 1
while i >= 0:
    new_arr = arr[i]
    i -= 1
    print(new_arr)

# Expected Output: 
# 13
# 11
# 9
# 7
# 5
# 3
# 1
