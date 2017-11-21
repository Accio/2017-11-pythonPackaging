#!/usr/bin/env python

import myPyPkg

help(myPyPkg.joke)
print(myPyPkg.joke())

help(myPyPkg.pythagorean)
print(myPyPkg.pythagorean(3,4))

help(myPyPkg.root)
print(myPyPkg.root(1,2,1))
print(myPyPkg.root(1,-2,1))
print(myPyPkg.root(1,0,-4))
print(myPyPkg.root(1,0,4))

## note that signPart is not exported
## print(myPyPkg.signPart(1,0,-4))
