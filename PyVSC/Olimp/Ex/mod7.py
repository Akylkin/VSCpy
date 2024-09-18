def mod2(num: str) -> int:
    result = ''
    flag = 0
    for nums in num:
        nextnum = int(str(flag)+nums)
        flag=nextnum % 8
        result+=str(nextnum//8)
    if ((len(result) > 1) and (result[0] == '0')):
        result = result[1:]
    return[result, flag]

def tentoeigth(strint: str, rlist: list = []):
    rlist.append(mod2(strint)[1])
    strint = mod2(strint)[0]
    if (strint == '0'):
        return rlist
    else:
        return tentoeigth(strint, rlist)

numlist = tentoeigth('27')
if sum(numlist) % 7 == 0:
    print('YEAH')
else:
    print("Yesn't")