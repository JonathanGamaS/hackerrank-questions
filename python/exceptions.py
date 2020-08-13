"""
You are given two values A and B.
Perform integer division and print A/B.
"""

def exception_training():
    total_inputs = int(input())
    for _ in range(total_inputs):
        a,b=input().split()
        try:
            print(int(a)//int(b))
        except (ZeroDivisionError,ValueError) as e:
            print('Error Code:',e)

exception_training()