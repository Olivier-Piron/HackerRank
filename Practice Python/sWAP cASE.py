# You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

def swap_case(s):
    s2 = ''
    for i in s:
        if ord(i) >= 65 and ord(i) <= 90:
            s2 += i.lower()
        elif ord(i) >= 97 and ord(i) <= 122:
            s2 += i.upper()
        else:
            s2 += i
    return s2
        

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)