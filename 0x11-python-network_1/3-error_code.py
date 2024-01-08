#!/usr/bin/python3
""" 3-error_code: Manages errors"""
import urllib.request
import urllib.error
import sys


def main():
    """main: sends a request with proper error management"""

    url = sys.argv[1]

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req) as response:
            context = response.read().decode('utf-8')
        print(context)
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")


if __name__ == "__main__":
    main()
