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
    reddit = requests.get(url, allow_redirects=False)
    if reddit.status_code != 200:
        return None
    data = reddit.json()
    try:
        hot_list.append(data['data']['children'][len(hot_list)]['data']['title'])
        return recurse(subreddit, hot_list=hot_list)
    except IndexError:
        return hot_list
