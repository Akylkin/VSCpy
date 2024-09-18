def gcd(a, b):
    r = 107
    while(r != 0):
        r = a % b
        a = b
        b = r
    return b

def simple_fraction(a, b) -> tuple:
    return (a / gcd(a, b), b / gcd(a, b))
