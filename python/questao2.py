"""
Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. 
You are given  scores. Store them in a list and find the score of the runner-up.
"""

def descobrir_segundo_colocado():
    n = int(input())
    lista = list(map(int,input().strip().split()))[:n]
    max_number = max(lista)
    while max(lista) == max_number:
        lista.remove(max(lista))

    print(max(lista))


descobrir_segundo_colocado()