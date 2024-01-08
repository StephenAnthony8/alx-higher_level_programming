#!/usr/bin/python3
""" 4-hbtn_status: fetches site"""
import requests
import sys


def main():
    """fetches from 'site"""
    site = 'http://0.0.0.0:5000/search_user'
    q = "" if len(sys.argv) == 1 else sys.argv[1]
    read_content = requests.post(site, data={'q': q})

    try:
        j_d = read_content.json()

        id_no, name = j_d.get('id'), j_d.get('name')
        if len(j_d) < 1:
            print("No result")

        elif None in [id_no, name]:
            print("Not a valid JSON")

        else:
            print(f"[{id_no}] {name}")

    except requests.exceptions.JSONDecodeError:
        print("No result")


if __name__ == """__main__""":
    main()
