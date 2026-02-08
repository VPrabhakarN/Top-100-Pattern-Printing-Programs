# Question : Write a program to print 'Rhombus Star Pattern'.

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_3
                *****
                 *****
                  *****
                   *****
"""
# Taking the input from the user 
size = 5

# Using for loop to print 'Rhombus Star Pattern'.
for i in range (0, size) :
    print(" "*i, end="")
    for j in range (0, size) :
        print("*", end="")
    print() 
    