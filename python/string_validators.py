"""
You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.
"""


def string_validator():
    s = input()
    print(bool(sum([1 for i in range(0,len(s)) if s[i].isalnum()])))
    print(bool(sum([1 for i in range(0,len(s)) if s[i].isalpha()])))
    print(bool(sum([1 for i in range(0,len(s)) if s[i].isdigit()])))
    print(bool(sum([1 for i in range(0,len(s)) if s[i].islower()])))
    print(bool(sum([1 for i in range(0,len(s)) if s[i].isupper()])))


if __name__ == '__main__':
    string_validator()