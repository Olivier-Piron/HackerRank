# You are given a two lists A and B. Your task is to compute their cartesian product AXB.

from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))

product = list(product(a,b))

print(' '.join(str(x) for x in product))
