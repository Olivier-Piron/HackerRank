# You are given a complex z. Your task is to convert it to polar coordinates.

import cmath

z = input()

print(abs(complex(z)))
print(cmath.phase(complex(z)))