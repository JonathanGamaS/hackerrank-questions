"""
Given the names and grades for each student in a class of N students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

"""

def listando_o_segundo_menor_score():
    marksheet = []
    for _ in range(0,int(input())):
        marksheet.append([input(), float(input())])

    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))



listando_o_segundo_menor_score()