# In `exercise.js` you have been provided with list of names.
# Write a program that logs a shouty greeting to each one.
# Your program should include a function that spells their name in uppercase,
# and a function that creates a shouty greeting.
# Log each greeting to the console.

# Add your code here

# Step1: create the "convertToUpperCase" function which takes a name as input
# The function whould convert the input to all upper case
# You might want to search on Google on how to convert a string to all upper case
def convertToUpperCase(name):
    return name.upper()

# Step 2, create an "greeting" function.
# This function should shout out greeting each of the name in all upper case
# Leverage the "convertToUpperCase" function to help you in converting the names to upper case
def greeting(name):  
    name2 = convertToUpperCase(name)
    print("HELLO " + name2)

# Testing Code
user1 = "Daniel"
user2 = "Irina"
user3 = "Mimi"
user4 = "Rob"
user5 = "Yohannes"

greeting(user1)
greeting(user2)
greeting(user3)
greeting(user4)
greeting(user5)


# Expected Output
# HELLO DANIEL
# HELLO IRINA
# HELLO MIMI
# HELLO ROB
# HELLO YOHANNES