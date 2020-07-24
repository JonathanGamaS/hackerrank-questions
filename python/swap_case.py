"""
You are given a string and your task is to swap cases. 
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""

def swap_case(s):
    new_string = ""
    for i in s:
        if i == i.upper():
            i = i.lower()
        elif i == i.lower():
            i = i.upper()
        else:
            continue
        new_string += i 
    return new_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)