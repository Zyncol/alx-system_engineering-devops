#!/usr/bin/python3
"""Module for the task 1"""


def top_ten(subreddit):
    """Queries the Reddit API and returns the top 10 hot posts"""
    import requests

    sub_infor = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_infor.status_code >= 300:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_infor.json().get("data").get("children")]
