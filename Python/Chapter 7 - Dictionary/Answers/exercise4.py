# Task: Write a Python program to list the properties(all the keys, not the values) of a Python dict.
# Hint: You can check the documentation of "dict.keys()" function.

def print_all_keys(inputDict):
    # Add your code here
    for k in inputDict.keys():
        print(k)




# DO NOT EDIT CODE BELOW
# Test Case：
student = {
    "name" : "David Rayy",
    "sclass" : "VI",
    "rollno" : 12 
}

print_all_keys(student)

# Expected Output:
# name
# sclass
# rollno