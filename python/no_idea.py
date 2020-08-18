"""
There is an array of N integers. 
There are also 2 disjoint sets, A and B, each containing M integers. 
You like all the integers in set A and dislike all the integers in set B. 
Your initial happiness is 0. For each I integer in the array, if i E A, you add 1 to your happiness. 
If i E B, you add -1 to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.
"""

def no_idea():
    n , m =(int(x) for x in input().split())
    N = list(int(x) for x in input().split())
    A,B=set(int(x) for x in input().split()), set(int(x) for x in input().split())
    hap=0
    test=set()
    for i in N:
        test.add(i)
        if test.issubset(A):
            hap+=1
        if test.issubset(B):
            hap-=1
        test.discard(i)
    print(hap)


no_idea()