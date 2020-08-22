"""
Apply your knowledge of the .add() operation to help your friend Rupal.
Rupal has a huge collection of country stamps. 
She decided to count the total number of distinct country stamps in her collection. She asked for your help. You pick the stamps one by one from a stack of N country stamps.
Find the total number of distinct country stamps.
"""


def resolving_rupal_problem():
    number_inserts = int(input())
    list_countrys = []
    for i in range(0,number_inserts):
        list_countrys.append(input())
    remove_duplicity = set(list_countrys)
    print(list_countrys)
    print(remove_duplicity)
    print(type(remove_duplicity))
    print(len(remove_duplicity))



resolving_rupal_problem()