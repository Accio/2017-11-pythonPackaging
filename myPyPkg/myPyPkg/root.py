import math

def root(a, b, c):
    """Return the roots of a quadratic equation"""
    s = signPart(a, b, c)
    try:
        root1 = -(b+s)/(2*a)
        root2 = -(b-s)/(2*a)
        return((root1, root2))
    except:
        print("Warning in root: No real roots available")


def signPart(a, b, c):
    """Hidden function serving root"""
    try:
        val = b**2 - 4*a*c
        res = math.sqrt(val)
        return(res)
    except:
        print("[inside signPart]: b**2-4*a*c<0: No real roots available")
