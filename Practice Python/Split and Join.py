# You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.

def split_and_join(line):
    li = line.split(' ')
    line2 = ''
    for i in li:
        line2 += i
        line2 += '-'
    return line2[:-1]

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)