"""
The students of District College have subscriptions to English and French newspapers. 
Some students have subscribed only to English, some have subscribed only to French, and some have subscribed to both newspapers.
You are given two sets of student roll numbers. 
One set has subscribed to the English newspaper, one set has subscribed to the French newspaper. 
Your task is to find the total number of students who have subscribed to both newspapers.
"""

def intersection_operation():
    total_inputs_first_sequence = int(input())
    first_sequence = set(input().split())
    total_inputs_second_sequence = int(input())
    second_sequence = set(input().split())
    both_subscribed = len(first_sequence & second_sequence)
    print(both_subscribed)
    return both_subscribed