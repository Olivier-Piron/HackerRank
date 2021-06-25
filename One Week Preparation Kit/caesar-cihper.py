# Complete the caesarCipher function in the editor below.

# caesarCipher has the following parameter(s):

# string s: cleartext
# int k: the alphabet rotation factor

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'caesarCipher' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. STRING s
#  2. INTEGER k
#

def caesarCipher(s, k):
    for i in range(len(s)):
        if s[i].islower():
            s = s[:i] + chr((ord(s[i])-97+k)%26 + 97) + s[i+1:]
        elif s[i].isupper():
            s = s[:i] + chr((ord(s[i])-65+k)%26 + 65) + s[i+1:]
    return s
                
                
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

    fptr.write(result + '\n')

    fptr.close()

