#!/usr/bin/python3
from sys import stderr
from sys import exc_info


def safe_function(fct, *args):
    try:
        return fct(*args)
    except Exception as e:
        print("Exception: {}".format(exc_info()[1]), file=stderr)
        return None
