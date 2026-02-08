# Question : Write a program to print 'Rectangle Star Pattern.

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_3
                *****
                *****
                *****
                *****
                *****
"""

# Taking input from the user 
length_ = int(input("Enter the length : "))
Width_ = int(input("Enter the width : "))

# Using nested for loop to print 'Ractangle star Pattern"
for i in range(0, Width_) :
    for i in range(0, length_) :
        print("*", end="")
    print()
