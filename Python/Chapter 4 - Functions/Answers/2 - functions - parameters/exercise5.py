# Write a function that takes a name (a string) and an age (a number) and returns a greeting (a string)

# Add your code here
def create_greeting(name,age):
    return "Hello, my name is {} and I'm {} years old".format(name,age)

greeting = create_greeting("Daniel", 30)

print(greeting)

# Expected Output
# Hello, my name is Daniel and I'm 30 years old
