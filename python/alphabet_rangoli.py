"""
You are given an integer, N. Your task is to print an alphabet rangoli of size N. 
(Rangoli is a form of Indian folk art based on creation of patterns.)
"""

def print_rangoli(size):
    l=[chr(96+size-i) for i in range(size)]
    l=["-".join("".join(l[:i])+l[i]+"".join(reversed(l[:i]))).center((4*size)-3,'-') for i in range(size)]
    print("\n".join(l[:size-1]+l[::-1]))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)    