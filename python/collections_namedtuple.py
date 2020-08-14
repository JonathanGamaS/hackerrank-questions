"""
Dr. John Wesley has a spreadsheet containing a list of student's ID's, marks, class and name.

Your task is to help Dr. Wesley calculate the average marks of the students.

average = sum of all marks / total students
"""
from collections import namedtuple


def solution_dr_problem():
    n = int(input())
    s1 = namedtuple('s1', " ".join(input().split()))
    print(sum([int(s1(*input().split()).MARKS) for _ in range(n)])/n)

solution_dr_problem()