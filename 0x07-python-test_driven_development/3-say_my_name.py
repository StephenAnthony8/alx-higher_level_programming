#!/usr/bin/python3
"""
    3-say_my_name - Name printing module
    say_my_name: function printing name
"""


def say_my_name(first_name, last_name=""):
    """
        say_my_name - prints out a name
        first_name: name[0]
        last_name: name[1]
    """
    output_str = None
    if isinstance(first_name, str) is False:
        output_str = "first_name"
    elif isinstance(last_name, str) is False:
        output_str = "last_name"
    if output_str is not None:
        raise TypeError("{} must be a string".format(output_str))
    print("{} {} {}".format("My name is",
                            first_name.strip(),
                            last_name.strip())
          )
