"""
Read four numbers, a, b, c, and d, and print the result of a^b + c^d.
"""

def problem_solution():
    a,b,c,d = (int(input()) for _ in range(4))
    print(pow(a,b)+pow(c,d))
    return pow(a,b)+pow(c,d)