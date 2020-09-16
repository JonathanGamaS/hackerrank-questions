"""
The National University conducts an examination of N students in X subjects.
Your task is to compute the average scores of each student.
"""

def zipped_solution():
    n, x = map(int, input().split()) 

    sheet = []
    for _ in range(x):
        sheet.append( map(float, input().split()) ) 

    for i in zip(*sheet): 
        print( sum(i)/len(i) )