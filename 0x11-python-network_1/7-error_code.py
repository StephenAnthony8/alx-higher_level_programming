#!/usr/bin/python3
""" 4-hbtn_status: fetches site"""
import requests
import sys


def main():
    """fetches from 'site"""
    url = sys.argv[1]
    read_content = requests.get(url)

    if (read_content.status_code >= 400):
        pr_str = f"Error code: {read_content.status_code}"
    else:
        pr_str = read_content.text
    print(pr_str)


if __name__ == """__main__""":
    main()
