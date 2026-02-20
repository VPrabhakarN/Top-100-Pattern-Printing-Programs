# Question : Write a program to print 'Basic Right Triangle Number Pattern'.

"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14
"""

# Taking an input from the user
size = int(input("Enter the size : "))




# Using for loop to print 'Basic Right Triangle Number Pattern'.
k = 0
for i in range(1, size+1) :
    for j in range(0, i) : 
        k += 1
        print(k, end=" ")
        
    print()