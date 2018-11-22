#!/bin/python

def mysum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])




def mysum(L):
    retrun 0 if not L else L[0] + mysum(L[1:])

def mysum(L):
    return L[0] if len(L) == 1 else L[0] + mysum(L[1:])

def mysum(L):
    first, *rest = L
    return first if not rest else first + mysum(rest)   #Use 3.0 ext seq assign



def mysum(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + mysum(L[1:])

L = [1, [2, [3, 4], 5], 6, [7, 8]]
def sumtree(L):
    tot = 0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot
