"""
Given an integer, n, and n space-separated integers as input, create a tuple, t, of those n integers. Then compute and print the result of hash(t).

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
"""
from builtins import hash


def creating_tuple_hash():
    ele = []
    n = int(input())
    x = input()
    temp = x.split(" ")
    for i in range(n):
        ele.append(int(temp[i]))
    t = tuple(ele)
    print(hash(t))




creating_tuple_hash()