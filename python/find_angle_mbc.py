"""
Point M is the midpoint of hypotenuse AC.
You are given the lengths AB and BC.
Your task is to find <MBC (angle 0°, as shown in the figure) in degrees.
"""

import math


def angle_finder():
    AB = int(input())
    BC = int(input())
    MBC = math.degrees(math.atan(AB/BC))
    answer = str(int(round(MBC)))+'°'
    print(answer)
    return answer


angle_finder()