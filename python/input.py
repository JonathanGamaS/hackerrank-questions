"""
You are given a polynomial P of a single indeterminate (or variable), x.
You are also given the values of x and k. Your task is to verify if P(x) = K.
"""

def input_solutiion():
    ui = input().split()
    x = int(ui[0])
    print(eval(input()) == int(ui[1]))