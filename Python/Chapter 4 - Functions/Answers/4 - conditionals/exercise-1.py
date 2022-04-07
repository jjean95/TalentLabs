####
#  Conditionals
#  ---------------------------------
#  Write a function to test if a provided number is negative or positive
#  - if number is less than zero, return the word "negative"
#  - if number is more or equal to zero, return the word "positive"
####

def negative_or_positive(number):
  # Add your code here
  if number < 0:
    return "negative"
  elif number >= 0:
    return "positive"
   

#### 
#  DO NOT EDIT BELOW THIS LINE
#  ---------------------------
####
number1 = 5
number2 = -1
number3 = 0

print(str(number1) + " is " + negative_or_positive(number1))
print(str(number2) + " is " + negative_or_positive(number2))
print(str(number3) + " is " + negative_or_positive(number3))

####
#  Expected Output
#  ---------------
#  5 is positive
#  -1 is negative
#  0 is positive
####
