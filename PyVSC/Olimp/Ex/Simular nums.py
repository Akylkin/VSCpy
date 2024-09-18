def nsmin(a: list, b: list) -> list:
    res = []
    for nums in a:
        if nums in b:
            res.append(nums)
            b.pop(b.index(nums))
    return res

def ns(*a:int) -> list:
    BFL = []
    res = []
    for num1 in a:
        numlist = []
        for num2 in str(num1):
            numlist.append(num2)
        BFL.append(numlist)
    res = nsmin(BFL[0], BFL[1])
    for i in range(2, len(BFL)):
        res = nsmin(res, BFL[i])
    return res

print(ns(1112222, 112222222, 2222111, 221))
