# Question : Write a program to print 'Hollow Square Star Pattern'.

"""
*****
*   *
*   *
*****
"""

# Taking the input from the user 
row = int (input("Enter the number of rows : "))
colomn = int (input("Enter the number of colomns : "))

for i in range(0, row) :
    for j in range(0, colomn) :
        if i == 0 or i == row-1 or j == 0 or j == colomn-1 :
            print("*", end="")
        else :
            print(" ", end="")  
    print()
