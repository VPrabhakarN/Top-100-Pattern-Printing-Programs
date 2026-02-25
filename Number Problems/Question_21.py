# Question : Write a program to print 'Basic incrementing Half Diamond Pattern(Inverted) initialised = 3'.

"""
3
4 4
5 5 5
6 6 6 6
5 5 5
4 4
3
"""
# Taking input
n = int(input("Size (Highest Peak): "))

start = 3

# Upper Part
for i in range(1, n + 1):
    value = start + i - 1
    for j in range(i):
        print(value, end=" ")
    print()

# Lower Part
for i in range(n - 1, 0, -1):
    value = start + i - 1
    for j in range(i):
        print(value, end=" ")
    print()
