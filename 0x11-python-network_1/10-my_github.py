#!/usr/bin/python3
""" 4-hbtn_status: fetches site"""
import requests
import sys


def main():
    """fetches from 'site"""
    username, pwd = sys.argv[1:]
    url = f"http://api.github.com/users/{username}"
    r = requests.get(url, auth=(username, pwd))

    print(r.json().get('id'))


if __name__ == """__main__""":
    main()
