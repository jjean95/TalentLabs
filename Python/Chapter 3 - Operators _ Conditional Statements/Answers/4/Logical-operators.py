####
#  Logical Operators
#  ---------------------------------
#  Using logical operators complete the unfinished statements.
#  The variables should have values that match the expected results.
####

# Do not change these two statement
htmlLevel = 8
cssLevel = 4

# Finish the statement to check whether HTML, CSS knowledge are above 5
# (hint: use the comparison operator from before)
htmlLevelAbove5 = htmlLevel > 5
cssLevelAbove5 = cssLevel > 5

# Finish the next two statement
# Use the previous variables and logical operators
# Do not "hardcode" the answers
cssAndHtmlAbove5 = cssLevelAbove5 & htmlLevelAbove5
cssOrHtmlAbove5 = cssLevelAbove5 | htmlLevelAbove5 

#### 
#  DO NOT EDIT BELOW THIS LINE
####  ---------------------------

print("Is Html knowledge above 5?", htmlLevelAbove5)
print("Is CSS knowledge above 5?", cssLevelAbove5)
print("Is Html And CSS knowledge above 5?", cssAndHtmlAbove5)
print(
  "Is either Html or CSS knowledge above 5?",
  cssOrHtmlAbove5
)

#### 
#  EXPECTED RESULT
#  ---------------
#  Is Html knowledge above 5? True
#  Is CSS knowledge above 5? False
#  Is Html And CSS knowledge above 5? False
#  Is either Html or CSS knowledge above 5? True
####
