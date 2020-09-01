"""
You are given a list of N lowercase English letters. 
For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.
Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""
import itertools


def problem_solution():
    a=int(input())
    b=input().split()
    c=int(input())
    count=0
    a1=list(itertools.combinations(list(b),c))
    x=len(a1)
    for i in a1:
        if 'a' in i:
            count+=1
    a2=count
    print(a2/x)