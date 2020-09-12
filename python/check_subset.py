"""
You are given two sets, A and B.
Your job is to find whether set A is a subset of set B.
"""

def check_subset_solution():
    for _ in range(int(input())):
        _, A = input(), set(map(int, input().split()))
        _, B = input(), set(map(int, input().split()))
        print(A.issubset(B))