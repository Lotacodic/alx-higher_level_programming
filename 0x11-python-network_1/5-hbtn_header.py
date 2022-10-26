#!/usr/bin/python3
"""
    A module that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
    found in the header of the response.
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    req = requests.get(argv[1])
    print(req.headers.get('X-Request-Id'))
