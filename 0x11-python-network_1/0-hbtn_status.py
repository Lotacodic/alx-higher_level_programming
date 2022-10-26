#!/usr/bin/python3
"""
    A module that fetches https://alx-intranet.hbtn.io/status
"""


if __name__ == '__main__':
    import urllib.request as req
    with req.urlopen('https://alx-intranet.hbtn.io/status') as e:
        page = e.read()
        print('Body response:')
        print('\t- type: {}'.format(type(page)))
        print('\t- content: {}'.format(page))
        print('\t- utf8 content: {}'.format(page.decode('utf-8')))
