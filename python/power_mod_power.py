"""
You are given three integers: a, b, and m, respectively. Print two lines.
The first line should print the result of pow(a,b). 
The second line should print the result of pow(a,b,m).
"""

def power_mod_power_solution():
    valor_1, valor_2, valor_3 = int(input()), int(input()), int(input())
    print(pow(valor_1,valor_2), pow(valor_1, valor_2, valor_3), sep='\n')
    return pow(valor_1,valor_2), pow(valor_1, valor_2, valor_3)