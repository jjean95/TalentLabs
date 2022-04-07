# Task: Print out all positive odd numbers up to n1

n1 = 19; 

# Add your code here:
i = 0
while i < n1:
    i += 1
    if i % 2 != 0:
        print(i)

# Expected Output:  
# 1
# 3
# 5
# 7
# 9
# 11
# 13
# 15
# 17
# 19