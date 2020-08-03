"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.
Ex: alison heck -> Alison Heck
Given a full name, your task is to capitalize the name appropriately.
"""
import os

def solve(s):
    b = ""
    count = 0
    for i in range(0,len(s)):
        if i == 0:
            x = s[i].upper()
            b += x
        elif s[i] == ' ':
            b += s[i]
            count = 1
        elif count == 1:
            x = s[i].upper()
            b += x
            count = 0
        else:
            b += s[i]
    return b


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)
    print(result)

    fptr.write(result + '\n')

    fptr.close()