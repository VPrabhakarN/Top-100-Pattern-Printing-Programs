# Question : Write a program to print 'Hollow Square Star Pattern'.

"""
*****
*   *
*   *
*****
"""
l = 5

for i in range(0, l) :
    for j in range(0, l) :
        if i == 0 or i == l-1 or j == 0 or j == l-1 :
            print("*", end="")
        else :
            print(" ", end="")  
    print()
