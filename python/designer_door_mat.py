"""
Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the following specifications:

Mat size must be NXM. (N is an odd natural number, and M is 3 times N.)
The design should have 'WELCOME' written in the center.
The design pattern should only use |, . and - characters.
"""


def designer_door_mat():
    n,m=map(int,input().split())

    for j in range (0,n-2,2):
        print((".|."*(j+1)).center(m,"-"))

    print("WELCOME".center(m,"-"))

    for i in range (n-2,0,-2):  
        print((".|."*i).center(m,"-"))