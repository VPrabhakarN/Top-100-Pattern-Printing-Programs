# Question : Write a program to print 'Hollow Pyramid Star Pattern'. 

"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_10
              *
             * *
            *   *
           *******
"""
# Taking input from the user
size = int(input("Enter the size : ")) # Number of rows

# Using the nested for loop 
for i in range(0, size) :
    
    # To print spaces (Reduce by -1 in every iteration)
    for j in range(0, size-i-1) :
        print(" ", end="")
    
    # To print stars (Increase by 2 in every iteration)
    for k in range(0, 2*i+1) :
        if(k==0 or i == 0 or k==2*i or i==size-1) :
            print("*", end="")
        else :
            print(" ", end="")
    print()

