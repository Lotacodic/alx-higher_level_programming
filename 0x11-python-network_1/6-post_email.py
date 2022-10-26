#!/usr/bin/python3
"""
    A module that takes in a URL and an email
    sends a POST request to the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import requests
    from sys import argv

    url = argv[1]
    val = {'email': argv[2]}
    req = requests.post(url, data=val)
    print(req.text)
