# Question : Write a program to print 'Half Diamond Star Pattern'. 

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_13
            *
            **
            ***
            ****
            ***
            **
            *
"""

# Taking an input from the user
size = int(input("Enter the size : ")) # Number of rows

# Using for loop 
for i in range(size) :
    if size//2 >= i :
        for j in range(i+1) :
            print("*", end="")
    else :
        for k in range(size-i, 0, -1) :
            print("*", end="")
            
    print()
    
    