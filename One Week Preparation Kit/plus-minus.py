# Complete the plusMinus function in the editor below.

# plusMinus has the following parameter(s):

# int arr[n]: an array of integers
# Print
# Print the ratios of positive, negative and zero values in the array. Each value should be printed on a separate line with 6 digits after the decimal. The function should not return a value.

# Input Format

# The first line contains an integer, n, the size of the array.
# The second line contains n space-separated integers that describe arr[n].

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    plus = 0
    minus = 0
    zero = 0
    for i in arr:
        if int(i) > 0:
            plus += 1
        elif int(i) < 0:
            minus += 1
        elif int(i) == 0:
            zero += 1
    sum_signs = plus + minus + zero
    print(plus/sum_signs)
    print(minus/sum_signs)
    print(zero/sum_signs)
            

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
