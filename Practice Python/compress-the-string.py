# You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the character 'c' with (X,c) in the string.

li = list(input())

prev = li[0]
cnt = 0
out = ''

for i in range(len(li)):
    if li[i] == prev:
        cnt +=1
    else:
        out += f'({cnt}, {prev}) '
        cnt = 1
        prev = li[i]
else:
    out += f'({cnt}, {prev})'

print(out)