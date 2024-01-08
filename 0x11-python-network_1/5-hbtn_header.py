#!/usr/bin/python3
""" 4-hbtn_status: fetches site"""
import requests
import sys


def main():
    """fetches from 'site"""
    site = sys.argv[1]
    read_content = requests.get(site)

    print(read_content.headers.get('X-Request-Id'))


if __name__ == """__main__""":
    main()
