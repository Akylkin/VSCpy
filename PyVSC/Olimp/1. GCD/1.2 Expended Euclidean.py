def exp_gcd(a: int, b:int) -> tuple:
    r = 123
    s0 = 1
    s1 = 0
    t0 = 0
    t1 = 1
    while(r != 0):
        q = a // b
        r = a - q * b
        s2 = s0 - q * s1
        t2 = t0 - q * t1
        a = b
        b = r

        s0 = s1
        s1 = s2

        t0 = t1
        t1 = t2
    return (a, s1, t1)

print(exp_gcd(240, 46))