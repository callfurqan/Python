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
students= ["Ali", "Afaq","Furqan","Haris", "Rizwan"]

# for break at a specific point
for students in students:
    if students == "Haris" :
        break;
    print(students)

for student in students:
    if student == "Haris":
        continue;
    print(students)
