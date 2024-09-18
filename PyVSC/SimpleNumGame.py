x = 10 # Кучка
p = 1 # Какой игрок сейчас ходит
p2 = 0 # Ход игрока 2
while(x != 0):
    if(x % 3 != 0):
        p = 1
        x -= 1
    else:
        print(f"Кучка = {x}")
        p = 2
        p2 = int(input("Твой ход - "))
        if p2 == 1 or p2 == 2 or p2 == 0:
            x -= p2
            print(f"Кучка = {x}")
        else:
            print("Ваш ход не соответсвует правилам, вы нечего не забираете.")
        p2 = 0
if p == 1:
    print("Player 1 wins!")
elif p == 2:
    print("Player 2 wins!")