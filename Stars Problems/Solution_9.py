# Question : Write a program to print 'Pyramid Star Pattern'

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_9
              *
             ***
            *****
           *******
"""

# Taking the input from the user 
size = int(input("Enter the size : "))  # Number of rows 

# Using the nested for loop 
for i in range(0, size) :
    
    # To print spaces (Reduce by -1 in every iteration)
    for j in range(0, size - i - 1 ) :
        print(" ", end="")
        
    # To print stars (Increase by +2 in every iteration)
    for k in range(0, 2*i+1) :
        print("*", end="")
        
    # To shift on new line 
    print()
    