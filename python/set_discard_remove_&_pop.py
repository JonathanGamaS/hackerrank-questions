"""
You have a non-empty set 8, and you have to execute N commands given in N lines.
The commands will be pop, remove and discard.
"""

def problem_solution():
    n = int(input())
    s = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        c = input().split()
        c.append('')
        exec('s.'+c[0]+f'({c[1]})')
    print(sum(s))