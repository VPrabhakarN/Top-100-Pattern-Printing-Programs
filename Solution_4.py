# Question : Write a program to print 'Rectangle Star Pattern'.

# Taking input from the user 
length = int(input("Enter the length : "))
width = int(input("Enter the width : "))

# Using for loop 
for i in range (0, width) :
    for j in range(0, length) :
        print("*", end="")
    print()