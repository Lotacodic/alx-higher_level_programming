#!/usr/bin/python3
"""A script that:
- takes your GitHub credentials (username and password)
- uses the GitHub API to display your id
"""
from sys import argv
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    authUser = HTTPBasicAuth(argv[1], argv[2])
    req = requests.get('https://api.github.com/user', auth=authUser)
    print(req.json().get('id'))
