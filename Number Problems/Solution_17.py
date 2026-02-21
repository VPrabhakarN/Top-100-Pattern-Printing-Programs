# Question : Write a program to print 'Basic Right Triangle Number Pattern (Inverted)'.

"""
15 14 13 12 11
10 9 8 7 
6 5 4
3 2
1
"""

# Taking an input from the user
size = int(input("Enter the size : ")) 

num = size*(size+1)//2

# Using for loop to print 'Basic Right Triangle Number Pattern (Inverted)'.
for i in range(size, 0, -1) :
    for j in range(i, 0, -1) :
        print(num, end=" ")
        num -= 1
        
    print()
