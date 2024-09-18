def triplepairless9() -> list:
    pairlist = []
    doublepairdict = {}
    for i in range(1, 7):
        for i1 in range(1, 10):
            for i2 in range(1, 10):
                if i + i1 + i2 < 9:
                    doublepairdict[str(i) + str(i1)] = 
                    pairlist.append(int(str(i) + str(i1) + str(i2)))
    return [pairlist, doublepairdict]

print(triplepairless9())
