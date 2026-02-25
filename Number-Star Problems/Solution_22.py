# Taking the size from the user 
size = int(input("Enter the size : "))  # Number of rows and colomns

num = 1

# Using for loop to print Basic incrementing Squared Number-Star Pattern
for i in range(0, size):
    for j in range(1, size + 1):

        if j < size:
            print(num, end="*")
        else:
            print(num, end="")

        num += 1

    print()