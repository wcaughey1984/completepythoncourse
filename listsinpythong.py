# 
# Title:    Lists in Python 
# Purpose:  Learning Python
# Author:   Billy Caughey 
# Date:     2020.07.02
#

friends = ["Rolf", "Bob", "Anne"]
print(friends)

print(len(friends))

friends1 = [
  ["Rolf", 24],
  ["Bob", 30],
  ["Anne", 27]
]

print(friends1[0][0])

friends.append("Jen")
print(friends)

friends.remove("Bob")
print(friends)

