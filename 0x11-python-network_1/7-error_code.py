#!/usr/bin/python3
"""
A script that:
- takes in a URL,
- sends a request to the URL
- displays the body of the response.
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    res = requests.get(argv[1])
    if res.status_code >= 400:
        print('Error code', res.status_code)
    else:
        print(res.text)
