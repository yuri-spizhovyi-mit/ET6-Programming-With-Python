#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Maximum Recursion Depth Exceeded

If a function calls itself without any conditional checks,
    it will continue calling itself until the stack overflows.

"""


def recursion_error(depth: int):
    if depth > 3:
        return "done recursing"
    else:
        print(depth)

        recursion_error(depth + 1)
    # the return statement will never be reached


print(recursion_error(0))
