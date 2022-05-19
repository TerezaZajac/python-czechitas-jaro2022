# ukol-10: Teplota ve městech
# Stáhni si soubor temperature.csv, který obsahuje informace o průměrné teplotě v různých městech v listopadu 2017.
# Vypiš si prvních několik řádků, ať si prohlédneš strukturu tabulky.
import pandas

temperature = pandas.read_csv('/Users/user/Desktop/programovani/FirstProgram/temperature.csv')
# print(temperature.shape)
temperature.info()

# Dále napiš následující dotazy:
# Dotaz na měření, která byla provedena v Praze. Je na datech něco zvláštního? Napadá tě, čím to může být? Zde je nápověda.

print(temperature.loc[temperature["City"] == "Prague"])

# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperature) vyšší než 80 stupňů.
print(temperature[temperature['AvgTemperature'] > 80])

# Dotaz na měření, ve kterých je teplota vyšší než 60 stupňů a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(temperature[(temperature['AvgTemperature'] > 60)& (temperature['Region'] == 'Europe')])

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 80 stupňů nebo menší než - 20 stupňů.
print(temperature[(temperature['AvgTemperature'] > 80)| (temperature['AvgTemperature']  < -20)])

# Bonus
# Nainstaluj si modul pytemperature a zkus si vytvořit nový sloupec, který bude obsahovat průměrnou templotu ve stupních Celsia.
# Ve svém programu nejprve proveď import modulu pytemperature. Nový sloupec pak přidáš do tabulky tak, že nalevo od = vložíš tabulku a název nového sloupce do hranatých závorek. Napravo pak můžeš provádět výpočty pomocí již existujících sloupců. Můžeš např. použít funkci f2c z modulu pytemperature, která převede teplotu ze stupňů Fahrenheita na stupně Celsia.

import pytemperature
temperature["AvgTemperatureCelsia"] = pytemperature.f2c(temperature["AvgTemperature"])
temperature.info()
# Nyní můžeš zpracovat následující příklady:
# Dotaz na měření, ve kterých je teplota (sloupec AvgTemperatureCelsia) vyšší než 30 stupňů Celsia.
print(temperature[temperature['AvgTemperatureCelsia'] > 30])

# Dotaz na měření, ve kterých je teplota vyšší než 15 stupňů Celsia a současně bylo měření provedeno v regionu (sloupec Region) Evropa (Europe).
print(temperature[(temperature['AvgTemperatureCelsia'] > 15)& (temperature['Region'] == 'Europe')])

# Dotaz na extrémní hodnoty, tj. měření, ve kterých je teplota vyšší než 30 stupňů Celsia nebo menší než -10 stupňů. Jsou některé hodnoty podezřelé?
print(temperature[(temperature['AvgTemperatureCelsia'] > 30)| (temperature['AvgTemperatureCelsia']  < -10)])

# Bonus 2
# Pokračuj ve své práci s informacemi o průměrných teplotách. Pokud jsi zpracoval/a první bonus, můžeš pracovat s teplotami ve stupních Celsia.
# Napiš následující dotazy:
# Dotaz na řádky z 13. listopadu 2017 (sloupec Day musí mít hodnotu 13).
print(temperature[temperature['Day'] == 13])
day_13 = temperature[temperature['Day'] == 13]

# Dotaz na řádky z 13. listopadu 2017 ze Spojených států amerických (sloupec Day musí mít hodnotu 13 a sloupec Country hodnotu US). Výsledek dotazu si ulož do nové tabulky a použij ji jako vstup pro následující dotaz.
us_13 = (day_13[day_13['Country'].isin(['US'])])

# Pro data z předchozího dotazu napiš dotaz na řádky ve městech (sloupec City) Washington a Philadelphia.
print(us_13[us_13['City'].isin(['Washington', 'Philadelphia'])])
