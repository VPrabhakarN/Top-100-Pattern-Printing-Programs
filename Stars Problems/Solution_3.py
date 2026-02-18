# Question : Write a program to print 'Rhombus Star Pattern'.

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_3
                *****
                 *****
                  *****
                   *****
"""
# Taking the input from the user 
rows = int(input("Enter the size of rows : "))
colomns = int(input("Enter the size of colomns : "))

# Using for loop to print 'Rhombus Star Pattern'.
for i in range (0, rows) :
    print(" "*i, end="")
    for j in range (0, colomns) :
        print("*", end="")
    print() 
    