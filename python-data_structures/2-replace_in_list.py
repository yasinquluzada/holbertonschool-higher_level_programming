#!/usr/bin/python3
def replace_in_list(my_list, idx, new_element):
    if idx < 0 or len(my_list) >= idx:
        return my_list
    my_list[idx] = new_element
    return my_list 
