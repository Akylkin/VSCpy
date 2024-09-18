import random
rnum = random.randint(0,9)
print("I have a number, it`s not more than 9. Guess it.")
yrnum = int(input("Yr`num? "))
while(yrnum != rnum):
    if(yrnum > rnum):
        print("Yr` number > my number")
    if(yrnum < rnum):
        print("Yr` number < my number")