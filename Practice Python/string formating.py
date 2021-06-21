# Given an integer, n, print the following values for each integer i from 1 to n:

# Decimal
# Octal
# Hexadecimal (capitalized)
# Binary

# The four values must be printed on a single line in the order specified above for each i from 1 to number. Each value should be space-padded to match the width of the binary value of number and the values should be separated by a single space.

def print_formatted(number):
    out = ''
    for i in range(number+1):
        out += f'{i}\t{oct(i)[2:]}\t{hex(i)[2:]}\t{bin(i)[2:]}\n'
    return out

print(print_formatted(17))