def gcd(a, b):
    r = 993
    while(r != 0):
        r = a % b
        a = b
        b = r
    return b

def triple_gcd(a, b, c):
    return gcd(gcd(a, b), c)
    