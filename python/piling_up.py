"""
There is a horizontal row of n cubes. The length of each cube is given. 
You need to create a new vertical pile of cubes. The new pile should follow these directions: if cubei is on top of cubej then sideLenghtj > sideLenghti.
When stacking the cubes, you can only pick up either the leftmost or the rightmost cube each time. 
Print "Yes" if it is possible to stack the cubes. Otherwise, print "No". Do not print the quotation marks.
"""
import sys
from collections import deque


def check_stack(n_d):
    ans = []
    
    while n_d:
        if n_d[0] > n_d[-1]:
            temp = n_d.popleft()
        elif n_d[0] < n_d[-1]:
            temp = n_d.pop()
        else:
            temp = n_d.popleft()
        ans.append(temp)

    
    temp = ans[:]
    temp.sort(reverse = True)
    if ans == temp:
        return 'Yes\n'
    else:
        return 'No\n'


def problem_solution():
    T = int(sys.stdin.readline())

    for i in range(T):
        input()
        n = deque(map(int, sys.stdin.readline().split()))
        sys.stdout.write(f'{check_stack(n)}')


if __name__ == '__main__':
    problem_solution()