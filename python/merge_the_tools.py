"""
Given S and K, print N/K lines where each line I denotes string Ui.
"""


def merge_the_tools(s, k):
    for i in range(0,len(s),k):
        s1=''
        for j in range(k):
            if s[i+j] not in s1:
                s1+=s[i+j]
        print(s1)


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)