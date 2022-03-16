# ukol-03: SMS brána
# Uvažuj, že píšeš jednoduchou aplikaci pro zasílání SMS zpráv. Napiš program, který provede následující činnosti:

# Zeptá se uživatele na číslo, kam chce zprávu zaslat a ověří, že číslo má správný formát.
# Zeptá se uživatele na zprávu, kterou chce zaslat. Následně vypíše, kolik zpráva bude stát.
# Tvůj program bude obsahovat dvě funkce:

# První funkce ověří délku telefonního čísla. Uvažuj, že telefonní číslo může být devítimístné nebo třináctimístné (pokud je na začátku předvolba "+420"). Nemusíte kontrolovat, zda uživatel zadal skutečně číslo, či zda jsou tam i jiné znaky. To jsme v kurzu zatím neřešili. Pokud je číslo platné, funkce vrátí hodnotu True, jinak vrátí hodnotu False.
# Druhá funkce spočte cenu zprávy. Uživatel platí 3 Kč za každých započatých 180 znaků.
# Tvůj program nejprve ověří pomocí první funkce správnost telefonního čísla. Pokud není platné, vypíše chybu, v opačném případě se zeptá na text zprávy a pomocí druhé funkce určí její cenu, kterou vypíše uživateli.

# Nápověda
# Pokud chcete zkontrolovat předvolbu, stačí využít podmínku"+420 in cislo, alternativně můžete využít indexy: Python umožňuje kromě jednoho znaku z řetězce získat i více znaků, a to pomocí dvojtečky. Pokud budete chtít získat první čtyři znaky, napište cislo[0:4]. Pak můžete vytvořit podmínku cislo[0:4] == "+420".

phone_number = input('Zadej sve telefoni cislo: ')
phone_message = ''
def phone_num_length():
    if len(phone_number) == 9 or len(phone_number) == 13:
        return True
    else: 
        return False

if phone_num_length() == True:
    phone_message = input('Zadej svoji zpravu: ')
else:
    print('spatne cislo')

#phone_message = input('Zadej svoji zpravu: ')
#print(phone_number)
#print(len(phone_number))

print(phone_message)

price = 0
def message_price():
    if 0 <= len(phone_message) <= 180:
        price += 3
    elif 180 < len(phone_message) >= 360:
        price += 6
    elif 360 < len(phone_message) >= 540:
        price += 9
    elif 540 < len(phone_message) >= 720:
        price += 12
    else:
        print('zprava je moc dlouha')
    return price
print(message_price())

