# You are given a string s and width w.
# Your task is to wrap the string into a paragraph of width w.

def wrap(string, max_width):
    out = ''
    i = 0
    while (i < len(string)):
        out += string[i:i+max_width]
        out += '\n'
        i += max_width
    return out

print(wrap('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 4))