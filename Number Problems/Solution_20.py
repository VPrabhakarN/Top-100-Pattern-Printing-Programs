# Question : Write a program to print 'Basic double incrementing Triangle Pattern initialised = 3'.

"""
3
4 5
6 7 8
9 10 11 12
"""

# Taking an input from the user
size = int(input("Enter the size : ")) #Number of rows

# initializing = 3
num = 3

# For loop to print 'Basic double incrementing Triangle Pattern initialised = 3'
for i in range(0, size) :
    for j in range(0, i+1) :
        print(num, end=" ")
        num += 1
    print()