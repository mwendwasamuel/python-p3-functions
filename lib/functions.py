#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
def greet(name):
    print("Hello, {}".format(name))
def greet_with_default(name=None):
    if name is None:
        print("Hello, programmer!")
    else:
        print("Hello, {}".format(name))
def add(a, b):
    return a + b
def halve(n):
    return n / 2