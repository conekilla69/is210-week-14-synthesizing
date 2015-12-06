#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""List comprehension"""


import task_01

def fibo():
    """"Returns the numbers of Fibonacci numbers to return.
        count (int): Number of Fibonacci numbers to return."""

    def fibo (count):
        while count < 0:
            count = []
            for count in fibo():
                count.append(count)
                return [count for count in fibo()]
