# Question : Write a program to print 'Basic incrementing Triangle Pattern initialised = 3'(Inverted).

"""
3
44
555
6666
77777

"""

# Taking an input from the user
size = int(input("Enter the size : ")) # Number of rows

num = 3 # Initialization = 3

for i in range(0, size) :
    for j in range(0, i+1) :
        print(num, end=" ")
    num += 1
        
    print()
