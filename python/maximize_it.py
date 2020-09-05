"""
You are given a function f(X) = X². You are also given K lists. The ith list consists of Ni elements.

You have to pick one element from each list so that the value from the equation below is maximized:
"""
import itertools


def maximize_it_solution():
    K,M=input().split()
    product1=[]
    for i in range(int(K)):
        list1=list(map(int,input().split()))
        product1.append(list1[1:len(list1)])
    list2=list(itertools.product(*product1))
    maxmize=[]
    for x in list2:
        crossp=(*x,)
        # print(p)
        p=sum([i**2 for i in crossp ])%int(M)
        maxmize.append(p)

    print(max(maxmize))