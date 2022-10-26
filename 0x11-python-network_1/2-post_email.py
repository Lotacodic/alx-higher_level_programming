#!/usr/bin/python3
"""
    A module that takes in a URL and an email
    sends a POST request to the passed URL with the email as a parameter
    and displays the body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    import urllib.request as req
    import urllib.parse as obj
    from sys import argv
    url = argv[1]
    val = {'email': argv[2]}
    data = obj.urlencode(val).encode('ascii')

    clientRequest = req.Request(url, data)
    with req.urlopen(clientRequest) as resp:
        print(resp.read().decode('utf-8'))
