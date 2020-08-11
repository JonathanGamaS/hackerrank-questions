"""
Ms. Gabriel Williams is a botany professor at District College. 
One day, she asked her student Mickey to compute the average of all the plants with distinct heights in her greenhouse.
"""

def average(array):
    lista_sem_duplicidade = set(array)
    soma_lista = sum(lista_sem_duplicidade)
    tamanho_lista_sem_duplicidade = len(lista_sem_duplicidade)
    resultado = soma_lista / tamanho_lista_sem_duplicidade
    return resultado

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)