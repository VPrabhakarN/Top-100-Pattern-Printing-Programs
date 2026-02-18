# Question : Write a program to print 'Basic Square Number Pattern'. 

# Taking the input from the user 
size = int(input("Enter the size : "))
number = int(input("Enter the number : "))

for i in range(0, size) :
    for j in range(0, size) :
        print(number, end=" ")         
    print()
    
