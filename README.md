# A minimalistic python package

The package was created following the example at https://python-packaging.readthedocs.io/en/latest/minimal.html.

## Usage

Call `make install` to install the package, and `make test` to run a script using the package

## Content

* `myPyPkg.joke()` prints a joke by Flying Circus. 
* `myPyPkg.pythagorean(a, b)` calculates the length of the hypotenuse `c`, given `a` and `b`, the lengths of the triangle's other two sides, using the quation `a^2+b^2=c^2`.
* `myPyPkg.root(a, b, c)` returns the roots of the quandratic equation `a*x**2+b*x+c=0`, and raises warning in case no real roots are available. I implemented an internal function, `signPart`, to test how to selectively export functions in __init.py__file.

All functions have a simple docstring.