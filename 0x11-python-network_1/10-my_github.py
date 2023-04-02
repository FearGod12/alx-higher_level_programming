#!/usr/bin/python3
''' takes your GitHub credentials (username and password)
and uses the GitHub API to display your id'''

import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    passwd = sys.argv[2]
    s = requests.Session()
    s.auth = (username, passwd)
    response = s.get('https://api.github.com/user')
    print(response.json().get('id'))
