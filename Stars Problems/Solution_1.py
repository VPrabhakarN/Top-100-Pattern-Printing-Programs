# Question : Write a program to print 'Square Star Pattern'.
"""
Docstring for Top-100-Pattern-Printing-Programs.Solution_1
                *****
                *****
                *****
                *****

"""
# Taking the input from the user
l = int(input("Enter the size : "))

#  Using for loop to print 'Sqaure Star Pattern'
for i in range(0, l) :
    for i in range(0, l) :
        print("*", end="")
    print("")