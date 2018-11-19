#!/bin/python
#Global scope
X = 99

def func(Y):
    #local scope
    Z = X + Y
    print Z
func(1)


def hider():
    open = 'spam'       #Local variable,hides built-in
    ...
    open('data.txt')    #This won't open a file now in this scope!
