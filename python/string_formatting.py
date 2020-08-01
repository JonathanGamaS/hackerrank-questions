"""
Given an integer, N, print the following values for each integer I from 1 to N:

1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary
"""


def print_formatted(number):
    b = len(str(bin(number)[2:]))
    for i in range(1,number+1):
        print("{0}{1}{2}{3}".format(str(i).rjust(b),str(oct(i)[2:]).rjust(b+1),str(hex(i)[2:].upper()).rjust(b+1),str(bin(i)[2:]).rjust(b+1)))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)


