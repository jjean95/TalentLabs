# Task: Write a Python program to list the key with values of a Python dict.
# Hint: You can check the documentation of "dict.items()" function.

def print_dict(inputDict):
    # Add your code here
    for k,v in inputDict.items():
        print(k + " : " + str(v))

# DO NOT EDIT CODE BELOW
# Test Case：
student = {
    "name" : "David Rayy",
    "sclass" : "VI",
    "rollno" : 12 
}

print_dict(student)

# Expected Output:
# name : David Rayy
# sclass : VI
# rollno : 12