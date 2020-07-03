# 
# Title:    Exercise - Nearby Friends 
# Purpose:  Coding exercise for learning python 
# Author:   Billy Caughey 
# Date:     2020.07.02 - Initial build 
# 

nearby_people = {"Rolf","Jen","Anna"}
user_friends = set() # this is an empty set

"""

In this task, ask the user for the name of a friend.

Add this name to user_friends set provided.

Print out the name if they are a nearby friend 

"""

new_friend = input("What is the name of your friend? ")
user_friends.add(new_friend)
nearby_user_friends = nearby_people.intersection(user_friends)
print(nearby_user_friends)
