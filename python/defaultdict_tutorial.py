"""
In this challenge, you will be given 2 integers, N and M. 
There are N words, which might repeat, in word group A. 
There are M words belonging to word group B. 
For each M words, check whether the word has appeared in group A or not. 
Print the indices of each occurrence of M in group A. If it does not appear, print -1.
"""
from collections import defaultdict


def creating_problem_solution():
    d = defaultdict(list)
    n,m=map(int,input().split())
    grA=[input() for i in range(n)]
    grB=[input() for i in range(m)]
    p=1
    for item in grA:
        if item in grB:
            d[item].append(p)
        p+=1
    for j in grB:
        if j in grA:
            print(*map(str,d[j]))
        else:
            print('-1')


creating_problem_solution()