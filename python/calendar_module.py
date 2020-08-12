"""
You are given a date. Your task is to find what the day is on that date.
"""
import calendar


def showing_year_of_input_date():
    mm, dd, yy = map(int, input().split())
    result = calendar.weekday(yy, mm, dd)
    print(calendar.day_name[result].upper())
    return calendar.day_name[result].upper()