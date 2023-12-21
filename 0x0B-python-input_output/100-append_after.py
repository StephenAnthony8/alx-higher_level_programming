#!/usr/bin/python3
"""
    100-append_after
    - Module containing function 'append_after'
"""


def append_after(filename="", search_string="", new_string=""):
    """
        append_after
        - inserts a line of text to  file after every specified string

        @filename: file to be modified
        @search_string: string to attach new_string to in file
        @new_string: string to attach
    """

    with open(filename, "r") as file:
        content = ""
        for line in file:
            content += line
            if search_string in line:
                content += new_string
    with open(filename, 'w') as file:
        file.write(content)


if __name__ == "__main__":
    append_after()
