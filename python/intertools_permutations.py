"""
You are given a string S.
Your task is to print all possible permutations of size K of the string in lexicographic sorted order.
"""

from itertools import permutations


def intertools_solution():    
    string, num = input().split()
    result = sorted(list(map(list, permutations(string, r = int(num)))))
    for i in result:
        print("".join(i))

intertools_solution()