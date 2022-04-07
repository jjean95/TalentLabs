# Please implement a program that ask for user's name
# After getting user's name, then you the program should say Hi to the user
# e.g. if the user's name is "Darren", your program should print "Hi, Darren"
# If the user did not put in a name or put in a empty name, your program should print "Hi, Guest"

print("What is your name?")

# Add your code here
# Step 1: collect user's input
name = input() or "Guest"

# Step 2: Greet User (Do not to use if statement)
print("Hi, {}".format(name))


