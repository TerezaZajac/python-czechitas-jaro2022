import random 

def roulette(row, bet):
    # if row > 3 or row < 1:
    #     return 'neplatna rada'
    if not (1<= row and row <= 3):
        return 'neplatna rada'

    x = random.randint(0,36)
    #print(x)
    if x == 0:
        return 0
    elif x % 3 == 1 and row == 1:
        return bet * 2
    elif x % 3 == 2 and row == 2:
        return bet * 2
    elif x % 3 == 0 and row == 3:
        return bet * 2
    else:
        return 0
    
row = input('Zvol si jednu ze tri rad: ')
bet = input('Vyska tve sazky: ')

print(roulette(int(row), int(bet)))