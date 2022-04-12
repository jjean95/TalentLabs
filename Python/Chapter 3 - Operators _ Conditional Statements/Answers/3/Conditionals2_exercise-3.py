####
#  Conditionals
#  ---------------------------------
#  Write a conditional statement that checks if a student has passed
#  - if the mark is 80 or higher then the grade is "A"
#  - if the mark is lower than 80 and greater than 60 then the grade is "B"
#  - if the mark is 60 or lower but no lower than 50 then the grade is "C"
#  - Otherwise the grade is "F"
####


grade1 = 49

# Add your code here
if grade1 >= 80:
    print(str(grade1) + ": A")
elif (grade1 < 80) and (grade1 > 60):
    print(str(grade1) + ": B")
elif (grade1 <= 60) and (grade1 >= 50):
    print(str(grade1) + ": C")
else:
    print(str(grade1) + ": F")

#  #### 
#  EXPECTED RESULT
#  ---------------
#  49: F
#  ####
