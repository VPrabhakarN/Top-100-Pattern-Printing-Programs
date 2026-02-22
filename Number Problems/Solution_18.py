# Question : Write a program to print 'Basic incrementing Triangle Pattern initialized = 3'.

# Taking an input from the user 
size = int(input("Enter the size : "))

num = size + 2

# Using for loop to print 'Basic incrementing Triangle Pattern initialized = 3'.
for i in range(size, 0, -1) :
    for j in range(i, 0, -1) :
        print(num, end=" ")
        
    if num >= 3 :
        num -= 1
    print()
    
 