#!/usr/bin/python3
"""A module to query an api usong recursion"""


import requests


def recurse(subreddit, hot_list=[]):
    """A function to query an api
    Args:
        subreddit: The subreddit to query
        hot_list: A list containing hot articles in the subreddit
    """

    url = "https://api.reddit.com/r/{}/top".format(subreddit)
    headers = {'User-Agent': "Mozilla/5.0"}

    reddit = requests.get(url, headers=headers, allow_redirects=False)
    if reddit.status_code != 200:
        return None
    data = reddit.json()
    try:
        hot_list.append(data['data']['children'][len(hot_list)]['da\
ta']['title'])
        return recurse(subreddit, hot_list=hot_list)
    except IndexError:
        return hot_list
