# Book List

# Task:
# Create an array of dicts, where each dict describes a book and has properties for the title (a string) and author (a string).

# There should be 4 books in the list:
# Harry Potter, J.K. Rowling
# Never Eat Alone , Keith Ferrazzi
# INSPIRED, Marty Cagan
# Zero to One, Peter Thiel



book_list = [
    # Add your code here
{"title":"Harry Potter", "author":"J.K. Rowling"},
{"title":"Never Eat Alone", "author":"Keith Ferrazzi"},
{"title":"INSPIRED", "author":"Marty Cagan"},
{"title":"Zero to One", "author":"Peter Thiel"}
]

# DO NOT EDIT CODE BELOW
# Test Case
for book in book_list:
    print(book["title"] + " by " + book["author"])



# Expected Output:
# Harry Potter by J.K. Rowling
# Never Eat Alone by Keith Ferrazzi
# INSPIRED by Marty Cagan
# Zero to One by Peter Thiel