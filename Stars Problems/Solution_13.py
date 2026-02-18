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
size = int(input("Enter the highest peak : ")) # highest peak

# Using for loop 
for i in range(0, size*2-1) :
    if i < size :
        for j in range(0, i+1):
            print("*", end="")
    else :
        for k in range((2*size)-i-1, 0, -1) :
            print("*", end="")      
    print()
    
    