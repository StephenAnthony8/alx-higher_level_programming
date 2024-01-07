#!/usr/bin/python3
""" 0-hbtn_status: fetches site"""
import urllib.request


def main():
    """fetches from 'site"""
    site = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(site) as response:

        d_read = response.read()
    body = f"Body response:"
    b_type = f"\t- type: {type(d_read)}"
    content = f"\t- content: {d_read}"
    b_utf = f"\t- utf8 content: {d_read.decode('utf-8')}"

    print(f"{body}\n{b_type}\n{content}\n{b_utf}")

if __name__ == """__main__""":
    main()



