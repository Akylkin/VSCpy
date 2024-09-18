def doublec_plus_one(l: list) -> list:
    l = l[::-1]
    flood = 0
    for i in range(len(l)):
        if l[i] == 0:
            flood = 0
            l[i] = 1
            break
        if l[i] == 1:
            flood = 1
            l[i] = 0
    if flood == 1:
        l.append(1)
    l = l[::-1]
    return l

print(doublec_plus_one([1, 1, 1, 1, 1]))