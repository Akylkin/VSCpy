def swap(i1: int, i2: int, orlist: list) -> list:
    list1 = orlist.copy()
    eliment1 = list1[i1]
    eliment2 = list1[i2]
    list1[i1] = eliment2
    list1[i2] = eliment1
    return list1

def permutate(list1, start):
    if start == len(list1):
        print(list1)
    for i in range(start, len(list1)):
        buff=swap(start, i, list1)
        permutate(buff, start + 1)

permutate([1, 2, 3, 4], 0)