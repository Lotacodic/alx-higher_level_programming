#!/usr/bin/python3
"""
display the value of the X-Request-Id variable
found in the header of the response.
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    with requests.get(argv[1]) as res:
        print(res.headers.get('X-Request-Id'))
