# Question : Write a program to print 'Hollow Rectangle Star Pattern'.

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_5
                    *****
                    *   *
                    *   *
                    *   *
                    *   *
                    *****
"""

# Taking an input from the user 
width = int(input("Enter the width : "))
height = int(input("Enter the height : "))

# Using for loop to print 'Hollow Rectangle Star Pattern'.
for i in range(0, width) :
    for j in range(0, height) :
        if i==0 or i == width-1 or j == 0 or j == height-1 :
            print("*", end="")
        else :
            print(" ", end="")
    print()