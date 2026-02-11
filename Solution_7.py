# Question : Write a program to print 'Mirrored Rhombus Star Pattern'

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_7
                    *****
                   *****
                  *****
                 *****
"""

# Taking the input from the user 
rows = int(input("Enter the number of rows : "))
colomns = int(input("Enter the number of colomns : "))

# Using the for loop to print 'Mirrored Rhombus Star Pattern'
for i in range(rows, 0, -1) :
    print(" "*i, end="")
    for i in range(colomns, 0, -1) :
        print("*", end="")
    print()
        

