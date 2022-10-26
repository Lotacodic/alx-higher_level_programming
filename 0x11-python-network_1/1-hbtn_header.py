#!/usr/bin/python3
"""
    A module that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
    found in the header of the response.
"""


if __name__ == '__main__':
    import urllib.request as req
    from sys import argv
    with req.urlopen(argv[1]) as e:
        print(e.headers.get('X-Request-Id'))
