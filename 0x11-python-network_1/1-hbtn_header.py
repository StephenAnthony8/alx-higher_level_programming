#!/usr/bin/python3
""" 1-hbtn_header: Requests value from URL"""
import urllib.request
import sys


def main():
    """ script takes in & sends request to URL and displays value"""
    url_name = sys.argv[1]

    with urllib.request.urlopen(url_name) as response:
        page = response.getheader('X-Request-Id')

    print(page)


if __name__ == "__main__":
    main()
