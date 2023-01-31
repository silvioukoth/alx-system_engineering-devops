#!/usr/bin/python3
"""This function queries reddit and returns the number of subscribers"""
import requests


def numbers_of_subscribers(subreddit):
    """"Returns the total numbers of subscribers on a given subreddit."""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "Users-agent": "linux:0x16.api.advanced:v1.0.0 (by /u/silvio_)"
    }
    response = requests.get(url, headers=headers, allow_reirects=False)
    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
