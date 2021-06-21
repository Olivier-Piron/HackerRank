#!/bin/python3

import math
import os
import random
import re
import sys

# You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.

def solve(s):
    s2 = ''
    li = s.split(' ')
    for i in li:
        s2 += i.capitalize() + ' '
    return s2[:-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()