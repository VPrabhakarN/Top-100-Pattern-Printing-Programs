# Question : Write a program to print 'Inverted Pyramid Star Pattern'.

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_11
            *******
             *****
              ***
               *        
""" 

# Taking an input from the user  
size = int(input("Enter the size : ")) #Number of rows

# Using nested for loop 
for i in range(size, 0, -1) :
    
     # Printing spaces 
    for k in range(0, size-i) :
        print(" ", end="")
    
    # Printing stars
    for j in range(0, 2*i-1) :
        print("*", end="")
    
    print()
