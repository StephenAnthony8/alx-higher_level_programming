#!/usr/bin/python3
""" 4-hbtn_status: fetches site"""
import requests


def main():
    """fetches from 'site"""
    site = 'https://alx-intranet.hbtn.io/status'
    read_content = requests.get(site)

    body = f"Body response:"
    b_type = f"\t- type: {type(read_content.content.decode())}"
    content = f"\t- content: {read_content.content.decode()}"

    print(f"{body}\n{b_type}\n{content}")


if __name__ == """__main__""":
    main()
