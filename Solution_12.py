# Question : Write a program to print 'Inverted Hollow Pyramid Star Pattern'. 

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_12
            *******
             *   *
              * *
               * 
"""

# Taking an input from the user 
size = int(input("Enter the size : "))

# Nested for loop to print 'Inverted Hollow Pyramid Star Pattern'. 
for i in range(size, 0, -1):
    
    # For loop to print spaces
    for j in range(size-i, 0, -1) :
        print(" ", end="")
        
    # For loop to print stars
    for k in range(2*i-1, 0, -1) :
        if k == 2*i-1 or k == 1 or i==size:
            print("*", end="")
        else :
            print(" ", end="")    
        
    print()