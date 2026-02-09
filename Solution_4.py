# Question : Write a program to print 'Rectangle Star Pattern'.

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_4
                    *** 
                    ***
                    ***
                    ***
                    ***
"""

# Taking input from the user 
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))

# Using for loop 
for i in range (0, width) :
    for j in range(0, length) :
        print("*", end="")
    print()