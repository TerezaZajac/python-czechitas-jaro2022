# Uvažuj, že vyvíjíš software pro službu, která nabízí streamování videa. Služba nabízí dva typy pořadů - filmy a seriály. Firma chce evidovat, které filmy a seriály nabízí a jejich žánry. Dále chce u filmů evidovat délku a u seriálů počet episod a délku jedné episody.

# Vytvoř program, který bude obsahovat tři třídy - Polozka, Film a Serial.
# Třída Polozka bude sloužit jako základ pro další třídy. Bude mít atributy určující název a žánr. Oba atributy nastav ve funkci __init__, žánr získej jako parametr funkce.
# Třída Film bude potomkem třídy Polozka. Film má kromě názvu a žánru atribut délka.
# Třída Serial bude potomkem třídy Polozka. Má kromě názvu a žánru atributy počet epizod a délka epizody.
# Všem třídám přidej funkci get_info, která vypíše informace o položce, resp. o filmu a seriálu. Funkce u třídy Polozka vypíše název a žánr. Následně tuto funkci využij ve funkcích u tříd Film a Serial a přidej k ní informaci o délce, resp. počtu episod.
# Po naprogramování si vytvoř alespoň jeden objekt reprezentující film a seriál a ověř, že vše funguje.

# Bonus:
# Pokračuj ve své práci pro streamovací službu. Služba nyní eviduje uživatele, kteří službu využívají. Vytvoř třídu Uzivatel, která bude mít atributy uzivatelske_jmeno a delka_sledovani, který udává celkovou délku pořadů, které uživatel zhlédl. Uživatelské jméno získej jako parametr a délka sledování je na začátku 0.

# Třídám Serial a Film přidej funkci get_celkova_delka, která vrátí celkovou délku filmu/seriálu (u seriálu je to počet episod násobený délkou jedné episody).

# Třídě Uzivatel přidej funkci pripocti_zhlednuti, která bude mít jeden parametr. Funkce zvýší atribut udávající celkovou délku sledávní o zadaný parametr.

# Vytvoř objekt, který reprezentuje nějakého uživatele. Následně zkus uvažovat situaci, že uživatel zhlédne film a seriál, které jsi vytvořil(a) jako objekty. Uživateli připočti délky děl k délce sledování, využij k tomu funkci get_celkova_delka u objektu a seriálu, abys zjistil(a), kolik minut (nebo hodin) videa celkem uživatel zhlédl.

# Nejjednodušší řešení je, pokud si u filmu/seriálu uložíš celkovou délku do pomocné proměnné a tuto pomocnou proměnnou potom předáš jako parametr funkci pripocti_zhlednuti.

class Polozka():
    def __init__(self, jmeno, zanr):
        self.jmeno = jmeno
        self.zanr = zanr
    
    def get_info(self):
        return f'nazev: {self.jmeno}, zanr: {self.zanr}. '

class Film(Polozka):
    def __init__(self, jmeno, zanr, delka):
        super().__init__(jmeno, zanr)
        self.delka = delka
    
    def get_info(self):
        return super().get_info() + f'Delka filmu je {self.delka} minut.' 

class Serial(Polozka):
    def __init__(self, jmeno, zanr, pocet_epizod, delka_epozido):
        super().__init__(jmeno, zanr)
        self.pocet_epizod = pocet_epizod
        self.delka_epizody = delka_epozido
    
    def get_info(self):
        return super().get_info() + f'Pocet epizod serialu je {self.pocet_epizod} a delka jedne epizody je {self.delka_epizody} minut.'



matrix = Film('Matrix', 'scifi', 131)

tbbt = Serial('The Big Bang Theory', 'sitcom', 24, 20)

print(matrix.get_info())
print(tbbt.get_info())

