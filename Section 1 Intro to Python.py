"""
Title:      Section 1 Intro to Python
Purpose:    Code and notes for learning Python
Author:     Billy Caughey
Date:       2020.06.25 - Initial Build
            2020.06.26 - Moved over to Atom
"""

#####################
# Numbers in Python #
#####################

integer_division = 13 // 5
print(integer_division)

remainder = 13 % 5
print(remainder)

x = 37
remainder = x % 2
print(remainder)

##################
# Python strings #
##################

my_string = "Hello, world!"
print(my_string)

string_with_quotes = "Hello, it's me."
print(string_with_quotes)

another_with_quotes = 'He said "You are amazing!" yesterday'
print(another_with_quotes)

same_quotes = "He said \"You are amazing!\" yesterday"
print(same_quotes)

multiline = """

My name is Jose. Welcome to my program.

"""
print(multiline)

name = "Jose"
greeting = "Hello, " + name
print(greeting)

# cannot add strings and numerics!

age = 34
age_as_string = str(age)
print("You are " + age_as_string)

############################
# Python String Formatting #
############################

age = 34
# age_as_str = str(34)
# print("You are " + age_as_str)
print(f"You are {age}")

name = "Jose"
greeting = f"How are you, {name}?"
print(greeting)

name = "Jose"
final_greeting = "How are you, {}?"
jose_greeting = final_greeting.format(name)
print(jose_greeting)

bob_greeting = final_greeting.format("Bob")
print(bob_greeting)

################################
# Getting user input in Python #
################################

# Get users name #
my_name = "Jose"
your_name = input("Enter your name: ")
print(f"Hello {your_name}. My is {my_name}")

# Telling the user how old he is #
# It's okay to nest a few functions
age = int(input("Enter your age: "))
months = age * 12
print(f"You have lived for {months} months")

##########
# Quiz 4 #
##########

# Question 1
your_name = input("Enter your name: ")
print(f"Hello {your_name}!")

# Question 2
