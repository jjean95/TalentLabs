# Write a function to check if the input word is the same if you read it forward and backward
# Tips: you can consider a string as an array (i.e. you can loop thru a string using loops and index)

def check_word(input):
    # Add your code here
    for i in range(0, int(len(input)/2)):
        if input[i] != input[len(input)-i-1]:
            return False
    return True
    

# DO NOT EDIT THE CODE BELOW
# Test Cases:

input1 = "abcdedcba"
print(check_word(input1))

# Expected Output 1: True


input2 = "apple"
print(check_word(input2))

# Expected Output 2: False