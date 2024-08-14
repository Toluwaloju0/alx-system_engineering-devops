#!/usr/bin/python3
"""A module to print the top ten titles of a subreddit"""


import requests


def top_ten(subreddit):
    url = "https://api.reddit.com/r/{}/hot".format(subreddit)

    reddit = requests.get(url, allow_redirects=False)
    if reddit.status_code != 200:
        print("None")
        return None

    data = reddit.json()

    try:
        for a in range(10):
            print(data['data']['children'][a]['data']['title'])
    except IndexError:
        pass
