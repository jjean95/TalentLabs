### Build a greeting python program

## Ask for user's name
print("What is your name?")
name = input() #store input into a variable

## Ask for user's age
print("What is your age?")
age = input()

## Greet the user and calculate his/her age next year
print("Hi " + name)
age_next_year = int(age) + 1 #convert into integer
print("You will be " + str(age_next_year) + " years old next year.") #convert integer into string
