"""
Print "True" or "False" for each test case without quotes.
"""
import re


def resolving_regex():
    for i in range(int(input())):
        try:
            re.compile(input())
            print("True")
        except:
            print("False")