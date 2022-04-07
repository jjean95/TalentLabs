####
#  Conditionals
#  ---------------------------------
#  Write a function that checks if a student has passed
#  - if the grade is less than 50 then return "failed"
#  - if 50 or higher then return "passed"
####


def student_passed(grade):
  # Add your code here
  if grade < 50:
    return "failed"
  else:
    return "passed"


#### 
# DO NOT EDIT BELOW THIS LINE
# ---------------------------
####

grade1 = 49
grade2 = 50
grade3 = 100

print("'" + str(grade1) + "': " + student_passed(grade1))
print("'" + str(grade2) + "': " + student_passed(grade2))
print("'" + str(grade3) + "': " + student_passed(grade3))

####
# Expected Output
# ---------------
# '49': failed
# '50': passed
# '100': passed
####
