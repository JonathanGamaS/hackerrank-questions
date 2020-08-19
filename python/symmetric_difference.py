"""
Given 2 sets of integers, M and N, print their symmetric difference in ascending order. 
The term symmetric difference indicates those values that exist in either M or N but do not exist in both.
"""

def resolving_problem():
    M = int(input())
    sn = input()
    sns = sn.split()
    sns_list = set(map(int, sns))

    N = int(input())
    numbers = input()
    separated_numbers = numbers.split()
    separated_numbers_set = set(map(int, separated_numbers))
    ans = list(sns_list.symmetric_difference(separated_numbers_set))
    ans.sort()

    for i in ans:
        print(i)