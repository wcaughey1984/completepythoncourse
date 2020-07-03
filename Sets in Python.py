#
# Title:    Sets in Python
# Purpose:  Learning about Sets in Python 
# Author:   Billy Caughey 
# Date:     2020.07.02 - Initial Build 
# 

# Sets don't hold order 
# Don't contain duplicate elements

art_friends = {"Rolf", "Anne"}
science_friends = {"Jen", "Charlie"}

art_friends.add("Jen")
print(art_friends)

art_friends.remove("Jen")
print(art_friends)

art_friends.add("Jen")

# Difference
art_but_not_science = art_friends.difference(science_friends)
print(art_but_not_science)

science_but_not_art = science_friends.difference(art_friends)
print(science_but_not_art)

# Symmetric Difference
not_in_both = art_friends.symmetric_difference(science_friends)
print(not_in_both)

# Intersection
art_and_science = art_friends.intersection(science_friends)
print(art_friends)

# Union 
all_friends = art_friends.union(science_friends)
print(all_friends)

