#!/usr/bin/python3
'''takes in a URL and an email, sends a POST request to the passed URL with
the email as a parameter, and displays the body of
the response (decoded in utf-8)'''


import urllib.request as request
import urllib.parse as parse
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = email = sys.argv[2]
    email = parse.urlencode({'email': email})
    with request.urlopen(url, data=email.encode()) as response:
        html = response.read()
        print(html.decode('utf-8'))
