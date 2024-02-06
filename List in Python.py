#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Furqan Riaz
#
# Created:     28/01/2024
# Copyright:   (c) Furqan Riaz 2024
# Licence:     <your licence>
#-------------------------------------------------------------------------------i = 2
# list functions in python
fruits= ["mango" ,"banana" ,"orange"]
fruits
#to add something in list in last
fruits.append("appple")
fruits
# to add value at a spcific index
fruits.insert(3, "dates")
fruits
#to add multiple values in list
fruits.extend (["cherry", "melons"])
fruits
#to count a value
fruits.count ("orange")

#to find index of the value
fruits.index("cherry")

#to delete whole list
fruits.clear()

#to copy ywhole list to a new list
fruits2= fruits.copy()

#to remove item from list
fruits.remove("apple")

#to find length of list
len (fruits)
