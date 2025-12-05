#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    """Return a new list with one element replaced at position idx.

    The original list is not modified. If idx is negative or
    out of range, a copy of the original list is returned.
    """
    if idx < 0 or idx >= len(my_list):
        # Invalid index: return a *copy* of the original list
        return my_list.copy()

    # Create a copy so the original list is not modified
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
