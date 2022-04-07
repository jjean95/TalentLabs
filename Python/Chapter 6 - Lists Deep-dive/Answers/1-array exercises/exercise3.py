# Task: Write a simple Python program to join all elements of the following array into a string with the Delimiter.
# Hint1: You might want to check out expected output before you start
# Hint2: You might want to check out the str.join() function
# 

def array_join(input_array, delimiter):
    # Add your code here
    lists = delimiter.join(input_array)
    return "\"{}\"".format(lists) #to insert parentheses outside the lists
    #return delimiter.join(input_array) #for not include parentheses
    
# DO NOT EDIT CODE BELOW
# Test Case :
myColor = ["Red", "Green", "White", "Black"]
print(array_join(myColor, ","))
print(array_join(myColor, "+"))

# Expected Output :
# "Red,Green,White,Black"
# "Red+Green+White+Black"