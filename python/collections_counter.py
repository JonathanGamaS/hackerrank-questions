"""
Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.
"""
from collections import Counter


def raghu_earn():
    input()
    c = Counter(input().split())
    sum = 0
    for _ in range(int(input())):
        n,p = input().split()
        if c[n]>0:
            sum += int(p)
            c[n] -= 1
    print(sum)

raghu_earn()