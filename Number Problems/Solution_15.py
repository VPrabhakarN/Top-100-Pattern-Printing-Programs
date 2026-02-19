# Question : Write a program to print 'Basic Square incrementing Pattern'.

"""
Docstring for Top-100-Pattern-Printing-Programs.Number Problems.Solution_15
                1 1 1 1 1 
                2 2 2 2 2
                3 3 3 3 3
                4 4 4 4 4
                5 5 5 5 5
                
"""

# Taking the input from the user 
size = int(input("Enter the size (Number of rows) : "))

# Using for loop to print the pattern
for i in range(1, size+1) :
    for j in range(0, size) :
        print(i, end=" ")
    print()