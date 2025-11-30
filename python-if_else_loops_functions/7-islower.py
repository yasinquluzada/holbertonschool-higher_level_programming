#!/usr/bin/python3
def islower(c):
    """Check if a character is a lowercase letter."""
    # ASCII: 'a' = 97, 'z' = 122
    return ord('a') <= ord(c) <= ord('z')
