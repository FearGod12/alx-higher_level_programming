#!/usr/bin/python3
'''takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter'''

import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""
    r = requests.post(url, data={'q': q})
    try:
        converted = r.json()
        if not converted:
            print("No result")
        else:
            the_id = converted.get('id')
            the_name = converted.get('name')
            print("[{}] {}".format(the_id, the_name))
    except (ValueError, requests.exceptions.JSONDecodeError):
        print("Not a valid JSON")
