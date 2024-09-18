def prime(num: int) -> bool:
    for nums in range(2, num-1):
        if num % nums == 0:
            return False
    return True

def hprimenum(num: int) -> int:
    if prime(num):
        return num
    i = 1
    numlist = []
    while i*i < num:
        i += 1
        if num % i == 0:
            if prime(i):
               return i

        
    
x = 600851475143

print(hprimenum(x))
        