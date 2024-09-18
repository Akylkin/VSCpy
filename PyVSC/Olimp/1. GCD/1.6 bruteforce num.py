def bruteen(a):
    i = 2
    primfac = []
    while(i*i <= a):
        while(a % i == 0):
            primfac.append(i)
            a = a // i
        i = i + 1
    if(a > 1):
        primfac.append(int(a))
    return primfac

print(bruteen(11))