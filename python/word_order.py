"""
You are given N words. Some words may repeat. For each word, output its number of occurrences. The output order should correspond with the input order of appearance of the word. 
See the sample input/output for clarification.
"""
from collections import OrderedDict


def problem_solution():
    d=OrderedDict()
    for _ in range(int(input())):
        x=input()
        d[x]=d.get(x,0)+1
    print(len(d.keys()))
    print(*d.values())