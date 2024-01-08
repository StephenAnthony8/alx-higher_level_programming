#!/usr/bin/python3
""" 4-hbtn_status: fetches site"""
import requests
import sys


def main():
    """fetches from 'site"""
    url, e_content = sys.argv[1:]
    read_content = requests.post(url, data={'email': e_content})

    print(read_content.text)


if __name__ == """__main__""":
    main()
