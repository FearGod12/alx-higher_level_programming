#!/usr/bin/python3
''' fetches https://alx-intrane.hbtn.io/status '''

if __name__ == "__main__":
    import requests
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    body = response.text
    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
