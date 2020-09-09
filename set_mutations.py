"""
You are given a set A and N number of other sets. 
These N number of sets have to perform some specific mutation operations on set A.
Your task is to execute those operations and print the sum of elements from set A.
"""

def problem_solution():
    n = int(input()) 
    set_A = set(input().split())
    for i in range(int(input())):
        cmd = input().split()
        set_B = set(input().split())
        eval('set_A.'+cmd[0]+'(set_B)')
    print(sum(map(int,set_A)))