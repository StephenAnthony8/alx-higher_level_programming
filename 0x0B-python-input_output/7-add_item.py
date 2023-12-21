#!/usr/bin/python3
"""
    7-add_item
    COntains
    - {Function}
"""
import sys
json_read = __import__('6-load_from_json_file').load_from_json_file
json_write = __import__('5-save_to_json_file').save_to_json_file


def args_append(filename):
    """
        args_append - adds commandline arguments to specified json file
        @filename: file to be modified
    """
    try:
        j_content = json_read(filename)
    except FileNotFoundError:
        j_content = []
    for i in sys.argv[1:]:
        j_content.append(i)
    json_write(j_content, filename)


def main():
    """
        main - contains the working functions
            - args_append
    """
    filename = 'add_item.json'
    args_append(filename)


if __name__ == "__main__":
    main()
