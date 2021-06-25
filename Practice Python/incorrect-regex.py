# You are given a string S.
# Your task is to find out whether S is a valid regex or not.

import re

n = int(input())

for i in range(n):
    try:
        re.compile(input())
        print(True)
    except re.error:
        print(False)