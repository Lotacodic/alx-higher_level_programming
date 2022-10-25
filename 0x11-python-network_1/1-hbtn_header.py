#!/usr/bin/python3
"""
display the value of the X-Request-Id variable
found in the header of the response.
"""


if __name__ == '__main__':
    from sys import argv
    from urllib import request

    url = argv[1]
    with request.urlopen(url) as response:
        print(response.info().get('X-Request-Id'))
