####
#  BOOLEAN WITH COMPARISON OPERATORS
#  ---------------------------------
#  Using comparison operators complete the unfinished statements.
#  The variables should have values that match the expected results.
####

studentCount = 16
mentorCount = 9
moreStudentsThanMentors = studentCount > mentorCount

roomMaxCapacity = 25
enoughSpaceInRoom = roomMaxCapacity >= studentCount + mentorCount

personA = "Daniel"
personB = "Irina"
sameName = personA == personB

### 
#  DO NOT EDIT BELOW THIS LINE
#  ---------------------------
print("Are there more students than mentors?", moreStudentsThanMentors)
print(
  "Is there enough space in the room for all students and mentors?",
  enoughSpaceInRoom
)
print("Do person A and person B have the the same name?", sameName)

####
#  EXPECTED RESULT
#  ---------------
#  Are there more students than mentors? True
#  Is there enough space in the room for all students and mentors? True
#  Do person A and person B have the the same name? False
####
