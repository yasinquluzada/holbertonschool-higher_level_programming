#!/usr/bin/python3


def uppercase(str):
    """Print a string in uppercase, followed by a new line."""
    result = ""
    for c in str:
        if 97 <= ord(c) <= 122:
            result += chr(ord(c) - 32)
        else:
            result += c
    print("{}".format(result))
