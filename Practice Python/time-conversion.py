# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    s = s.strip()

    res = ''
    if s[-2:] == 'AM':
        if int(s[0:2]) >= 12:
            res = str(int(s[0:2])-12).zfill(2) + s[2:-2]
        else:
            res = s[0:-2]
    elif s[-2:] == 'PM':
        if int(s[0:2]) < 12:
            res = str(int(s[0:2])+12).zfill(2) + s[2:-2]
        else:
            res = s[0:-2]    
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
