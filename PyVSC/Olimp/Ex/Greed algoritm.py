def doublesort(listor: list) -> list:
    listor.sort(reverse=True)
    list1 = []
    list2 = []
    s1 = 0
    s2 = 0
    for nums in listor:
        if s1 <= s2:
            if nums > 0:
                s1 += nums
                list1.append(nums)
            else:
                s2 += nums
                list2.append(nums)
        else:
            if nums > 0:
                s2 += nums
                list2.append(nums)
            else:
                s1 += nums
                list1.append(nums)
    print(list1, s1, list2, s2)
    return None

bruh = [3, 5, -2, 10, 2, 3, 5]
doublesort(bruh)