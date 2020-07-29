"""
You are given a partial code that is used for generating the HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.
"""


def text_alignment():
    t = int(input()) 
    c = 'H'
    for i in range(t):  
        print((c*i).rjust(t-1)+c+(c*i).ljust(t-1))
    for i in range((t+1)):
        print((c*t).rjust(((3*t)-1)//2)+(c*t).rjust(4*t))   
    for i in range((t+1)//2):   
        print((c*(t*5)).rjust(((11*t)-1)//2))   
    for i in range((t+1)):
        print((c*t).rjust(((3*t)-1)//2)+(c*t).rjust(4*t))
    for i in range(t):  
        print((c*(t-i-1)).rjust((5*t)-1)+c+(c*(t-i-1)).ljust(t-1))


text_alignment()