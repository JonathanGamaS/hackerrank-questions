"""
You are given a complex Z. Your task is to convert it to polar coordinates.
"""
import cmath


def polar_coordinates():
    q=complex(input())
    print(abs(q),cmath.phase(q),sep="\n")

polar_coordinates()