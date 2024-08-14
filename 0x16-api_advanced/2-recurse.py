#!/usr/bin/python3
"""A module to query an api usong recursion"""


import requests

def recurse(subreddit, hot_list=[]):
    """A function to query an api
    Args:
        subreddit: The subreddit to query
        hot_list: A list containing hot articles in the subreddit
    """

    url = "http://api.reddit.com/r/{}/top".format(subreddit)
    reddit = requests.get(
