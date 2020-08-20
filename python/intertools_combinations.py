"""
You are given a string S.
Your task is to print all possible combinations, up to size K, of the string in lexicographic sorted order.
"""

from itertools import combinations


def makeing_solution():
    a = input().split()
    for i in range(1, int(a[1]) + 1):
        print (*(''.join(j) for j in combinations(sorted(a[0]), i)), sep = '\n')