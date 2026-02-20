# Question : Write a program to print 'Basic Right Triangle Number Pattern'.

# Taking an input from the user
size = int(input("Enter the size : "))




# Using for loop to print 'Basic Right Triangle Number Pattern'.
k = 0
for i in range(1, size+1) :
    for j in range(0, i) : 
        k += 1
        print(k, end="")
        
    print()