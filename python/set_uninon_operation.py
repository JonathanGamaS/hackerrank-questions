"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. 
The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
"""

def problem_solution():
    number_inputs_group_a = int(input())
    roll_english = list(map(int,input().split()))[:number_inputs_group_a]
    number_inputs_group_b = int(input())
    roll_french = list(map(int,input().split()))[:number_inputs_group_b]
    total = set(roll_english).union(set(roll_french))
    total_lenght = len(total)
    print(total_lenght)
    return total_lenght


if __name__ == '__main__':
    problem_solution()