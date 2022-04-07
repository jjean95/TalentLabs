# Task: Make a filtered list of all the people who are over 18

def age_over_18(arr):
  # Add your code here
  new_list = []
  for people in arr:
    if people["age"] > 18:
      new_list.append(people)
  return new_list
  
# DO NOT EDIT CODE BELOW
# Test Cases:
print(age_over_18([
  { "name": "Peter Chan", "age": 22 },
  { "name": "Darren Chiu", "age": 12 },
  { "name": "Paul Lau", "age": 5 },
  { "name": "Erika Lee", "age": 30 },
  { "name": "Anthony Wong", "age": 16 } 
]))

# Expected Output: 
#[ { name: 'Peter Chan', age: 22 },
#  { name: 'Erika Lee', age: 30  }]