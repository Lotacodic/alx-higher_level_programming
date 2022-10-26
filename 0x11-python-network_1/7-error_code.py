#!/usr/bin/python3
"""
    A module that takes in a URL  sends a request to the URL
    and displays the body of the response (decoded in utf-8).
"""


if __name__ == '__main__':
    import requests
    from sys import argv
    req = requests.get(argv[1])

    if req.status_code < 400:
        print(req.text)
    else:
        print('Error code: {}'.format(req.status_code))
