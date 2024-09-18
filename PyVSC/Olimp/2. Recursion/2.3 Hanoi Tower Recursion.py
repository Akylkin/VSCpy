def hanoi(n, pole1, pole2): 
    if n == 1:
        print(f'{pole1} -> {pole2}')
        return 0
    p = 6 - pole1 - pole2
    hanoi(n-1, pole1, p)
    print(f'{pole1} -> {pole2}')
    hanoi(n-1, p, pole2)

hanoi(40, 1, 3)