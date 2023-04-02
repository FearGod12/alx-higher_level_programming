#!/usr/bin/python3
'''takes 2 arguments and list 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails'''

import sys
import requests

if __name__ == "__main__":
    REPO = sys.argv[1]
    OWNER = sys.argv[2]
    url = f'https://api.github.com/repos/{OWNER}/{REPO}/commits'
    response = requests.get(url)
    number = 0
    for each in response.json()[:10]:
        print("{}: {}".format(each['sha'], each['commit']['author']['name']))
