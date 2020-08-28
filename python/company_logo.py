"""
A newly opened multinational brand has decided to base their company logo on the three most common characters in the company name. 
They are now trying out various combinations of company names and logos based on this condition. 
Given a string s, which is the company name in lowercase letters, your task is to find the top three most common characters in the string.

Print the three most common characters along with their occurrence count.
Sort in descending order of occurrence count.
If the occurrence count is the same, sort the characters in alphabetical order.
"""

import sys
from collections import Counter

def problem_solution():
    
    S = sys.stdin.readline()

    ans = Counter(sorted(S))

    count = 0
    while count < 3:
        max_key = max(ans, key=ans.get)
        sys.stdout.write(f'{max_key} {ans[max_key]}\n')
        del ans[max_key]
        count+=1
    

if __name__ == '__main__':
    main()
