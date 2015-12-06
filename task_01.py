#!/usr/bin/env python
#-*- coding: utf-8 -*-
"""Fibonacci sequence"""


def xfibo():
    """Numnber of sequences to be returned.

    count (int): number of Fibonacci sequences to return."""

    def xfibo(count):
        iteration = 0
        while iteration < count:
            yield iteration
            iteration +=1
            
