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

def numsofd(a):
    primfac = [1, 2, 2, 3, 3, 3]
    numdict = {}
    for nums in primfac:
        if nums not in numdict:
            numdict[nums] = 1
        else:
            numdict[nums] = numdict[nums] + 1
    print(numdict)

numsofd(1)