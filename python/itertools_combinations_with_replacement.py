"""
You are given a string S.
Your task is to print all possible size K replacement combinations of the string in lexicographic sorted order.
"""
from itertools import combinations_with_replacement


def itertools_solution():
    a = input().split()
    print(*(''.join(j) for j in combinations_with_replacement(sorted(a[0]), int(a[1]))), sep = '\n')