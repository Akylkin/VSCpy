def simple_gcd(a, b) -> str:
    while(a%b != 0):
        r = a % b
        a = b
        b = r
    if b == 1:
        return('Yes')
    else:
        return('No')
