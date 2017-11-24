#!/usr/bin/env python

import myPyPkg
import argparse

parser = argparse.ArgumentParser(description="Calculate the length of the hypotenuse of a right triangle, using the pythagorean theorem")

parser.add_argument('a', help='Numeric value of a', type=float)
parser.add_argument('b', help='Numeric value of b', type=float)

opts = parser.parse_args()

c = myPyPkg.pythagorean(opts.a, opts.b)

print(c)
