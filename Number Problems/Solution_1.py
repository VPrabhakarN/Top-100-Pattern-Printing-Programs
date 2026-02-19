# Question : Write a program to print 'Basic Square Number Pattern'. 

"""
Docstring for Top-100-Pattern-Printing-Programs.Number Problems.Solution_1
                1 1 1 1 1
                1 1 1 1 1
                1 1 1 1 1
                1 1 1 1 1 
                1 1 1 1 1 
"""

# Taking the input from the user 
size = int(input("Enter the size : "))
number = int(input("Enter the number : "))

for i in range(0, size) :
    for j in range(0, size) :
        print(number, end=" ")         
    print()
    
