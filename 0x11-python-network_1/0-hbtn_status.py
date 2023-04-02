#!/usr/bin/python3
''' https://alx-intranet.hbtn.io/status '''

if __name__ == "__main__":
    import urllib.request
    url = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
    print("\t- type: {}".format(html.__class__))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html.decode("utf-8")))
