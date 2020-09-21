"""
You are given a spreadsheet that contains a list of N athletes and their details (such as age, height, weight and so on). 
You are required to sort the data based on the the Kth attribute and print the final resulting table. 
Follow the example given below for better understanding.
"""

def athlete_sort_solution():
    N,M = map(int,input().split())
    rows = [list(map(int,input().split())) for i in range(N)]
    i = int(input())
    rows = sorted(rows, key=lambda x:x[i])
    for i in rows:
        print(*i)