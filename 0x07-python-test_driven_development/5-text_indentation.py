#!/usr/bin/python3
"""
    4-text_indentation - module printing 2 new lines per delimiter
"""


def text_indentation(text):
    """
        text_indentation - substitutes delimiters with new lines
        @text: string to be modified
    """
    if isinstance(text, str):
        delimiters = ['.', '?', ':']
        text_list = list(text)
        for i in range(len(text_list)):
            if text_list[i] in delimiters:
                text_list[i] = "{}{}".format(text_list[i], "(replace_this_line)")
        text = "".join(text_list)
        x = text.split("(replace_this_line)")
        for i in range(len(x)):
            x[i] = x[i].strip(" ")
        text = "\n\n".join(x)
        print("{}".format(text), end="")
    else:
        raise TypeError("{}".format("text must be a string"))
