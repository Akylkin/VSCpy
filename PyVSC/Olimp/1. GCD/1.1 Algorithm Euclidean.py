def gcd(a, b) -> int:
    while(a%b != 0):
        r = a % b
        a = b
        b = r
    return b

def lcd(a, b) -> int:
    return a*b/gcd(a,b)

print(gcd(1071, 462))