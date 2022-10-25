#!/usr/bin/python3
"""
A script that:
- takes in a URL
- sends a POST request to the passed URL
- takes email as a parameter
- displays the body of the response
"""


if __name__ == '__main__':
    from sys import argv
    import requests

    with requests.post(argv[1], data={'email': argv[2]}) as res:
        print(res.text)
