"""
You are given a set A and n other sets.
Your job is to find whether set A is a strict superset of each of the N sets.
Print True, if A is a strict superset of each of the N sets. Otherwise, print False.
A strict superset has at least one element that does not exist in its subset.
"""

def check_strict_superset_solution():
    prime_set=set(input().split())
    flag=False
    for _ in range(int(input())):
        sample_set = set(input().split())
        flag=prime_set.issuperset(sample_set)
        if flag==False:
            break
    print(flag)