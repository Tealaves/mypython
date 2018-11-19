#/bin/python
X = 99
def setX(new):
    global X
    X = new

import first
first.setX(88)
