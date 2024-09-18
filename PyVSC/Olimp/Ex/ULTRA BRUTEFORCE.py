def wholehalf(l: list, res: float, total:list = [], best:list = []):
    if (res <= 0):
        if (abs(res) < best[1]):
            best[0] = total.copy()
            best[1] = abs(res)
        if (abs(res-total[-1])) < best[1]:
            best[0] = total[:-1].copy()
            best[1] = abs(res-total[-1])        
        return []
    if ((res > 0) and (len(l) == 0)):
        if (abs(res) < best[1]):
            best[0] = total.copy
            best[1] = abs(res)
        return []
    for i in range(len(l) - 1):
        new_t = total.copy()
        new_t.append(l[i])
        wholehalf(l[i+1:], res - l[i], new_t, best)

liste = [3, 2, 5, 4, 6, 8, 5, 2, 4, 5, 6, 7]

best = [[], sum(liste)]
wholehalf(liste, sum(liste) / 2, [], best)
print(best)