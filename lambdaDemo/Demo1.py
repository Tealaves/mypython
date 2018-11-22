#!/bin/python

L = [lambda x: x ** 2,
        lambda x: x ** 3,
        lambda x: x ** 4]
for f in L:
    print(f(2))
print(L[0](3))


def f1(x): return x ** 2
def f2(x): return x ** 3
def f3(x): return x ** 4

L1 = [f1, f2, f3]

for f in L:
    print(f(2))
print(L1[0](3))
