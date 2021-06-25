# You are given two values  and .
# Perform integer division and print .

# Input Format

# The first line contains T, the number of test cases.
# The next T lines each contain the space separated values of a and b.

n = int(input())

for i in range(n):
    x = input().split(' ')
    
    try:
        a = int(x[0])
        b = int(x[1])
        try:
            print(a//b)
        except ZeroDivisionError:
            print("Error Code:", "integer division or modulo by zero")
    except ValueError as e:
        print("Error Code:",e)