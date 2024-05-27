#!/usr/bin/python3
"""Module for  the task number 0"""


def number_of_subscribers(subreddit):
    """Queries the Reddit API and returns the number of subscribers"""
    import requests

    sub_infor = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_infor.status_code >= 300:
        return 0

    return sub_infor.json().get("data").get("subscribers")
