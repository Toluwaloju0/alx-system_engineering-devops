#!/usr/bin/python3
"""A module to get the api of reddit"""


import requests
import json


def number_of_subscribers(subreddit):
    """A function to get the number of subscribers for a ressit page
    Args:
        subreddit: The reddit page
    """
    url = "https://api.reddit.com/r/{}/about".format(subreddit)
    reddit = requests.get(url)
    if reddit.url != url or reddit.status_code != 200:
        return 0
    data = reddit.json()

    return data['data']['subscribers']
