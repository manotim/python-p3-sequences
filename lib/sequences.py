#!/usr/bin/env python3

def print_fibonacci(length):
    empty_list = []
    a, b = 0, 1
    while(len(empty_list) < length):
        empty_list.append(a)
        a, b = b, a + b
    print (empty_list)
    pass