# Question : Write a program to print 'Triangle Star Pattern'

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_8
                *
                **
                ***
                **** 
"""

# Taking the value from the user 
rows = int(input("Enter the size of rows : "))
colomns = int(input("Enter the size of colomns : "))

# Using for loop to print 'Triangle Star Pattern'
for i in range (0, rows) :
    for j in range(0, colomns) :
        if j <= i :
            print("*", end="")
        else :
            print(" ", end="")
    print()