def gcd(a, b) -> int:
    while(a%b != 0):
        r = a % b
        a = b
        b = r
    return b

def lcd(a, b) -> int:
    return a*b//gcd(a,b)

def grooplcd(*a):
    buf = lcd(a[0], a[1])
    for i in range(2, len(a)):
        buf = lcd(buf, a[i])
    return buf

print(grooplcd(10, 15, 30, 60))