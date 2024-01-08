#!/usr/bin/python3
""" 1-hbtn_header: Requests value from URL"""
import urllib.request
import urllib.parse
import sys


def main():
    """main: sends a POST request"""

    url, email_addr = sys.argv[1:]

    values = {'email': email_addr}
    data = urllib.parse.urlencode(values)
    data = data.encode('ascii')
    try:
        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            context = response.read().decode('utf-8')
        print(context)
    except ValueError:
        pass


if __name__ == "__main__":
    main()
