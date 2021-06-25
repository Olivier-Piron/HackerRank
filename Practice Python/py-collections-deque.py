# Perform append, pop, popleft and appendleft methods on an empty deque d.

# The first line contains an integer N, the number of operations.
# The next N lines contains the space separated names of methods and their values.

from collections import deque

d = deque()

for i in range(int(input())):
    argv = input().split(' ')
    method = argv[0]
    
    if method == 'append':
        d.append(argv[1])
    elif method == 'appendleft':
        d.appendleft(argv[1])
    elif method == 'pop':
        d.pop()
    elif method == 'popleft':
        d.popleft()

print(' '.join(d))