# Task: Print out the sum of the arrays on each index
# Tips: You can add a new item to an empty list with x.append(newitem) function. Feel free to search for more exmaples of this.

array1 = [1, 3, 5]
array2 = [2, 4, 6]


result = []
# Add your code here:
i = 0
while (i < len(array1)) and (i < len(array2)):
    result.append(array1[i]+array2[i])
    i += 1

# DO NOT EDIT BELOW
print(result)

# Expected Output: 
# [3, 7, 11]

