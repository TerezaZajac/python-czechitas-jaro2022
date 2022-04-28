# ukol-08: Prodej vstupenek
# Vytvoř program na prodej vstupenek do letního kina. Ceny vstupenek jsou v tabulce níže.

# Datum	                    Cena
# 1. 7. 2021 - 10. 8. 2021	250 Kč
# 11. 8. 2021 - 31. 8. 2021	180 Kč
# Mimo tato data je středisko zavřené.

# Tvůj program se nejprve zeptá uživatele na datum a počet osob, pro které uživatel chce vstupenky koupit. Uživatel zadá datum ve středoevropském formátu. Převeď řetězec zadaný uživatelem na datum pomocí funkce datetime.strptime().

# Pokud by uživatel zadal příjezd mimo otevírací dobu, vypiš, že letní kino je v té době uzavřené. Pokud je letní kino otevřené, spočítej a vypiš cenu za ubytování.

# Data lze porovnávat pomocí známých operátorů <, >, <=, >=, ==, !=. Tyto operátory můžeš použít v podmínce if. Níže vidíš příklad porovnání dvou dat. Program vypíše text "První datum je dřívější než druhé datum.".

# from datetime import datetime
# prvni_udalost = datetime(2021, 7, 1)
# druha_udalost = datetime(2021, 7, 3)
# if prvni_datum < druhe_datum:
#   print("Druhá událost se stala po první události")

from datetime import datetime
visitor_date_str = input('Zadejte datum (ve středoevropském formátu) navstevy kina: ')
visitor_number = input('Zadejte pocet vstupenek: ')

visitor_date_str = visitor_date_str.replace(' ','')
visitor_date = datetime.strptime(visitor_date_str, "%d.%m.%Y")

if datetime(2021, 7, 1)<=visitor_date<=datetime(2021, 8, 10):
    cena = 250
elif datetime(2021, 8, 11)<=visitor_date<=datetime(2021, 8, 31):
    cena = 180
else:
    cena = 0
    print('Neplatne datum')

cena_final = cena*int(visitor_number)
print(f'Vstupenky jste rezervovali na {visitor_date_str}. Celkova cena za vstupenky je: {cena_final} kc.')


