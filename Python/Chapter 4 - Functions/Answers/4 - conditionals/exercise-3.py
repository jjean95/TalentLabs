####
#  Conditionals
#  ---------------------------------
#  Write a function that checks if a student has passed
#  - if the mark is 80 or higher then the grade is "A"
#  - if the mark is lower than 80 and greater than 60 then the grade is "B"
#  - if the mark is 60 or lower but no lower than 50 then the grade is "C"
#  - Otherwise the grade is "F"
####

# define your function here
def calculate_grade(number):
    if number >= 80:
        return "A"
    elif (number < 80) and (number > 60):
        return "B"
    elif (number <= 60) and (number > 50):
        return "C"
    else:
        return "F"


####
# DO NOT EDIT BELOW THIS LINE
# ---------------------------
####

grade1 = 49
grade2 = 90
grade3 = 70
grade4 = 55

print("'" + str(grade1) + "': " + calculate_grade(grade1))
print("'" + str(grade2) + "': " + calculate_grade(grade2))
print("'" + str(grade3) + "': " + calculate_grade(grade3))
print("'" + str(grade4) + "': " + calculate_grade(grade4))

#### 
#  EXPECTED RESULT
#  ---------------
# '49': F
# '90': A
# '70': B
# '55': C
####