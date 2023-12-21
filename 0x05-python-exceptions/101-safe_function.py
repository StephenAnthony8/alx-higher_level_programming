#!/usr/bin/python3
from sys import stderr


# safe_function - executes a function safely
# fct: function passed in
# args: fct args
# Return: None on fail or rtn on pass
def safe_function(fct, *args):
    rtn = None
    try:
        rtn = fct(*args)
    except Exception as e:
        stderr.write("{} {}\n".format("Exception:", str(e)))
        return (None)
    return (rtn)
