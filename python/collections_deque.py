"""
Perform append, pop, popleft and appendleft methods on an empty deque d.
"""
from collections import deque


def problem_solution():
    try:
        d = deque()
        for i in range(int(input())):
            cmd,*args = input().split()
            getattr(d, cmd)(*args)
        print(' '.join(d))
    except Exception as e:
        raise e