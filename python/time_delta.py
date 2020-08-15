"""
When users post an update on social media,such as a URL, image, status update etc., other users in their network are able to view this new post on their news feed. Users can also see exactly when the post was published, i.e, how many hours, minutes or seconds ago.

Since sometimes posts are published and viewed in different time zones, this can be confusing. You are given two timestamps of one such post that a user can see on his newsfeed in the following format:

Day dd Mon yyyy hh:mm:ss +xxxx

Here +xxxx represents the time zone. Your task is to print the absolute difference (in seconds) between them.
"""

import datetime


def time_delta(t1, t2):
    t=int(input())
    for _ in range(t):
        s1=str(input())
        s2=str(input())
        f="%a %d %b %Y %H:%M:%S %z"
        d1=datetime.datetime.strptime(s1,f)
        d2=datetime.datetime.strptime(s2,f)
        print(int(abs(d1-d2).total_seconds()))