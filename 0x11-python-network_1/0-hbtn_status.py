#!/usr/bin/python3
""" Python script that fetches https://alx-intranet.hbtn.io/status """


if __name__ == '__main__':
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        con = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(con)))
        print("\t- content: {}".format(con))
        print("\t- utf8 content: {}".format(con.decode('utf-8')))
