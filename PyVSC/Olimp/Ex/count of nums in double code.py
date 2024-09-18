def mod2(num: str) -> int:
    result = ''
    flag = 0
    for nums in num:
        nextnum = int(str(flag)+nums)
        if (nextnum % 2 == 0):
            flag=0
            result+=str(nextnum//2)
        if (nextnum % 2 != 0):
            flag=1
            result+=str(nextnum//2)
    if ((len(result) > 1) and (result[0] == '0')):
        result = result[1:]
    return[result, flag]


def count1nums(strint: str, sum: int = 0):
    sum += mod2(strint)[1]
    strint = mod2(strint)[0]
    if (strint == '0'):
        return sum
    else:
        return count1nums(strint, sum)

print(count1nums('100000'))